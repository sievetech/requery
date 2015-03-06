
function useUrlParams() {
    params = window.location.search;
    params = params.replace('?', '');
    params = params.split('&');
    data = {};
    _.each(params, function (param) {
        var values = param.split('=');
        data[values[0]] = values[1];
        $('[name="' + values[0] + '"]').val(values[1]);
    });
}

function autoRun(){
    if(data.force && data.force.toLowerCase() == 'true') {
        $('#id_run').click();
    }
}

function download(){
    $('.table').tableExport({type:this.dataset.type,escape:'false'});
}