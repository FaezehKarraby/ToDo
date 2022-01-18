function status(status){
    document.getElementById('status').value='';
    let param = status;
    send_request(param)
}

function subject(subject){
    document.getElementById('subject').value='';
    let param = subject;
    send_request(param);
}

function send_request(param){
    $.ajax({
        method: 'GET',
        url: 'api/get_status?' + param,
        beforeSend: function (){
            console.log('before send');
        },
        success: function (result){
            update_table(result);
            console.log('after send');
        },
        error:function (){
            console.log('error');
        }
    });
}

function update_table(data){
    let row;
    let all_rows='';

    Object.keys(data).forEach(key => {
        elem = data(key);
        row = '<tr><td>' + elem['status'] + '</td>' + '</tr>';
        all_rows = all_rows + row;
    });
    $('#myTable tbody').html(all_rows)
}