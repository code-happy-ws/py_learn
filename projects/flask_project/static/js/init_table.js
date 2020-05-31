
var $table =  $('#tb_table');
var globaltitle = {};
var emptydata = {};
var configjson ;

function inittitle(gtitle) {
    var firstcolumns = [
        {
            field: "check", title: "", checkbox: true, formatter: function (value, row, index) {
//                return row.index = index + 1; //返回行号
        }
        },
        {
            field: "id", title: "ID", align: "center", edit: false, formatter: function (value, row, index) {
//                console.log(index)
//                return row.index = index ; //返回行号
            return index;
        }
        }
    ]

    var lastcolumns = {
        field: "id", title: "操作", align: "center", formatter: function (value, row, index) {

            var html = '';
            html += '<a href="javascript:void(0);" onclick="removeData(' + row.id + ')" ><li class="glyphicon glyphicon-remove"></li>删除</a>';
            return html; //返回行号
        }
    }

    for (var a in gtitle) {
        var obj = {
            editable: {
                type: 'text',
                mode: "popup",//popup
                title: '',
                disabled: true,
                emptytext: '无',
//                    validate:function () {
//
//                    }
            }
        }
        obj.field = gtitle[a];
        obj.title = a;
        obj.editable.title = a;

        firstcolumns.push(obj);
    }

    firstcolumns.push(lastcolumns);

    return firstcolumns;

}


var TableInit = function (data,columns) {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $table.bootstrapTable({
            url: '',         //请求后台的URL（*）
            data:data,
            method: 'get',                      //请求方式（*）
            toolbar: '#toolbar',                //工具按钮用哪个容器
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
            pagination: true,                   //是否显示分页（*）
            sortable: false,                     //是否启用排序
            sortOrder: "asc",                   //排序方式
            queryParams: '',//传递参数（*）
            sidePagination: "client",           //分页方式：client客户端分页，server服务端分页（*）
            pageNumber:1,                       //初始化加载第一页，默认第一页
            pageSize: 10,                       //每页的记录行数（*）
            pageList: [10,50, 100,300,500],        //可供选择的每页的行数（*）
//                search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
            strictSearch: true,
            showColumns: true,                  //是否显示所有的列
            showRefresh: true,                  //是否显示刷新按钮
            minimumCountColumns: 2,             //最少允许的列数
            clickToSelect: true,                //是否启用点击选中行
//                height: 500,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
            uniqueId: "ID",                     //每一行的唯一标识，一般为主键列
//                showToggle:true,                    //是否显示详细视图和列表视图的切换按钮
            cardView: false,                    //是否显示详细视图
            detailView: false,                   //是否显示父子表
            columns:columns,
            onClickRow: function (row) {
               console.log(row)
            },
        });
    };

    return oTableInit;
};
//初始化页面上面的按钮事件
var ButtonInit = function () {
    var oInit = new Object();
    var postdata = {};

    oInit.Init = function () {
        $('#btn_add').click(addcolumns)
        $('#btn_delete').click(deletecolumns)
        $('#btn_edit').click(editcolumns)
        $('#identitys').change(changeidentitys)

    };

    return oInit;
};

$('#btn_get').click(function () {
    var table = $table.bootstrapTable('getData');
    console.log(table)
})

function  addcolumns() {
    var table = $table.bootstrapTable('getData'),
        length = table.length;;
    var type = $('#identitys input:radio:checked').val();
    var empty = cloneObj(configjson[type].data);
    empty.id = length +1;

    $table.bootstrapTable('load',table );
    $table.bootstrapTable('selectPage', 1); //Jump to the first page
    $table.bootstrapTable('prepend', empty);

}
function deletecolumns() {
    var obj =$table.bootstrapTable('getSelections');
    var ids = $.map(obj, function (row) {
        return row.id;
    });
    if(ids.length>0){
        $table.bootstrapTable('remove', {field: 'id', values: ids});
    }else {
        alert("请至少选择一行删除")
    }
}

function editcolumns() {
    $table.find('.editable').editable('toggleDisabled');
}

function  removeData(index) {
    $table.bootstrapTable('remove', {field: 'id', values: [index]});
}

//    $table.on("click-row.bs.table",function(e, row, $element) {
//        var  index= $element.data('index');
//        alert(index);
//    });

function importfile(file) {//导入
    var f = file.files[0];
    $("#excelfile").val(f.name);
    var wb;//读取完成的数据
    var rABS = false; //是否将文件读取为二进制字符串
    var ie = IEVersion();
    if(ie != -1 && ie != 'edge'){
        if(ie<10){
            return;
        }else{
            rABS = true;
        }
    }

    if(checkfilename(file)){
        var reader = new FileReader();
        reader.onload = function(e) {
            var data = e.target.result;
            if(rABS) {
                wb = XLSX.read(btoa(fixdata(data)), {//手动转化
                    type: 'base64'
                });
            } else {
                wb = XLSX.read(data, {
                    type: 'binary'
                });
            }
            var result = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]]);

            resoveresult(globaltitle,result);
        };

        if(rABS) {
            reader.readAsArrayBuffer(f);
        } else {
            reader.readAsBinaryString(f);
        }
    }


}

function resoveresult(config,list) {
    $table.bootstrapTable('showLoading');
    var rs= [];
    if(list.length>0){
        for(var one in list){
            var obj = {};
            for(var index in config){

                var key = list[one][index];
                if(!key){
                    obj[config[index]]="";
                }else {
                    obj[config[index]] = key;
                }

            }
            obj.id = Number(one);
            rs.push(obj);
        }
        $table.bootstrapTable('load',rs );
    }
    $table.bootstrapTable('hideLoading');
}

function getjson(url) {
    $.ajaxSetup({async:false});
    var rs;
    $.getJSON(url, function(json){
        rs = json;
    });
    return rs;
}

function changeidentitys() {
    $("#FileInput").val('');
    $("#excelfile").val('');
    var type = $('#identitys input:radio:checked').val();
    for (var m in configjson) {
        if (configjson[m].type == type) {
            globaltitle = configjson[m].title;
            $table.bootstrapTable('destroy');
            initTable();
        }
    }
}

function initTable() {
    var columns = inittitle(globaltitle);
    //1.初始化Table
    var oTable = new TableInit([],columns);
    oTable.Init();
}
$(function () {
    configjson = getjson('config/data.json');
    globaltitle = configjson[1].title;
    initTable();
    //2.初始化Button的点击事件
    var oButtonInit = new ButtonInit();
    oButtonInit.Init();

});
