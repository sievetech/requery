
function useUrlParams() {
    params = window.location.search;
    params = params.replace('?', '');
    params = params.split('&');
    data = {};
    _.each(params, function (param) {
        var values = param.split('=');
        $('[name="' + values[0] + '"]').val(values[1]);
    });
}