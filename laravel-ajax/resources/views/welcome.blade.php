@extends('layouts.master')

@section('title')
    Laravel
@endsection

@section('content')
    <h2>Laravel + AJAX Demo</h2>
    <div class="row">
        <div class="col-lg-5">
            <button class="btn btn-warning" id="getRequest">GET Request</button>
        </div>

        <div class="col-lg-5">
            <h3>Post Request</h3>
            <form action="#" id="register">
                {{csrf_field()}}
                <label for="firstname"></label>
                <input type="text" id="firstname" class="form-control">

                <label for="lastname"></label>
                <input type="text" id="lastname" class="form-control">
                <br>
                <input type="submit" value="Register" class="btn btn-primary">
            </form>
        </div>
    </div>

    <div class="row">
        <div class="col-lg-5">
            <div id="getRequestData"></div>
        </div>
        <div class="col-lg-5">
            <div id="postRequestData"></div>
        </div>
    </div>

@endsection

@section('scripts')
    <script type="text/javascript">
        $.ajaxSetup({
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            }
        });
        $(document).ready(function () {
            var printed = false;
            $('#getRequest').click(function () {
                $.get('/api/sample-get', function (data) {
                    if (!printed) {
                        $('#getRequestData').append(data);
                        printed = true;
                    }
                });

                $.ajax({
                    type: 'GET',
                    url: '/api/sample-get',
                    success: function (res) {
                        console.log(res);
                        $('#getRequestData').html(res);
                    }
                });
            });

            $('#register').submit(function () {
                var fname = $('#firstname').val();
                var lname = $('#lastname').val();

                var dataString = "firstname=" + fname + "&lastname" + lname;
                $.ajax({
                    type: 'POST',
                    url: '/api/sample-post',
                    data: dataString,
                    success: function (data) {
                        console.log(data);
                        $('#postRequestData').html(data);
                    },
                });

            })
        });
    </script>
@endsection
