import webbrowser

import os

import re



# file: fresh_tomatoes.py



# Styles and scripting for the page

main_page_head = '''

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="utf-8">

    <title>Fresh Tomatoes!</title>



    <!-- Bootstrap 3 -->

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/\

3.1.0/css/bootstrap.min.css">

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/\

3.1.0/css/bootstrap-theme.min.css">

    <link href='https://fonts.googleapis.com/css?family=Fontdiner+Swanky|\

Allerta+Stencil' rel='stylesheet' type='text/css'>

    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>

    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/\

bootstrap.min.js"></script>

    <style type="text/css" media="screen">

        /*

        * {

            outline: 1px solid red !important;

        }

        */



        body {

            padding-top: 80px;

        }



        img {

            cursor: pointer;

        }



        #trailer .modal-dialog {

            margin-top: 200px;

            width: 640px;

            height: 480px;

        }



        .hanging-close {

            position: absolute;

            top: -12px;

            right: -12px;

            z-index: 9001;

        }



        #trailer-video {

            width: 100%;

            height: 100%;

        }



        .movie-tile {

            margin-bottom: 20px;

            padding-top: 20px;

        }



        .movie-tile:hover {

            background-color: white;

        }



        .scale-media {

            padding-bottom: 56.25%;

            position: relative;

        }



        .scale-media iframe {

            border: none;

            height: 100%;

            position: absolute;

            width: 100%;

            left: 0;

            top: 0;

            background-color: white;

        }



        /* 'plot': i.e., the storyline */

        .plot {

            color: white;

            font-weight: normal;

            margin-bottom: 0;

            padding-bottom: 0;

        }



        .navbar-brand {

            color: green;

            font-size: 2em;

            font-family: 'Fontdiner Swanky', cursive;

            font-weight: normal;

            background-color: rgb(252,22,0);

        }



        .navbar-brand:enabled {

            color: green;

        }



        .navbar-brand:hover {

            color: blue;

        }



        .navbar {

            text-align: center;

            background-color: rgb(252,22,0);

        }



        /* table of the stars' names */

        .table0 {

             display: none;

             border: thick dotted yellow;

             text-align: center;

             position: absolute;

             top: 20px;

             left: 80px;

             cursor: pointer;

        }



        /* names of up to four stars */

        .data0,

        .data1,

        .data2,

        .data3 {

            background-color: #ddf;

            font-family: 'Allerta Stencil', sans-serif;

            color: red;

            font-size: 2em;

            font-weight: 400;

        }



    </style>

    <script type="text/javascript" charset="utf-8">

        // Data 'overImage' allows us to tell when the cursor is over

        // the movie art (as opposed to over the movie-tile)

        // so we can display the modal *only* then.

        $(document).on('mouseover', '.image', function(event) {

            $(this).data("overImage", "yes");

            var image_width = $(this).width();

            var image_height = $(this).height();

            var table = $(this).siblings('.table0');

            table.css('width', image_width);

            table.css('height', image_height);

            table.focus();

            var data = $(this).siblings().find('td');

            data.each(function () {

                $(this).css('width', image_width);

            });

            table.toggle(true);

        });

        $(document).on('mouseout', '.image', function(event) {

            var table = $(this).siblings('.table0');

            table.toggle(false);

            $(this).focus();

            $(this).data("overImage", "no");

        });



        $(document).on('mouseover', '.table0', function(event) {

            $(this).focus();

            $(this).toggle(true);

            var image = $(this).siblings('.image');

            image.blur();

            image.data("overImage", "yes");

        });



        $(document).on('mouseout', '.table0', function(event) {

            $(this).toggle(false);

            $(this).blur();

            $(this).siblings('.image').focus();

            $(this).siblings('.image').data("overImage", "no");

        });



        // This 'hides' the plot summary by making its text white

        // unless the movie title is being moused over.

        // Necessary because if the plot summary is not present

        // (though white) at all times, the images will jump around

        // when the plot summary is introduced.

        $(document).on('mouseover', '.title', function(event) {

            var plotId = $(this).siblings('.plot').css('color','black');

        });



        $(document).on('mouseout', '.title', function(event) {

            var plotId = $(this).siblings('.plot').css('color','white');

        });



        // Pause the video when the modal is closed

        $(document).on('click', '.hanging-close, .modal-backdrop, .modal',

                function (event) {

            // Remove the src so the player itself gets removed, as this is the

            // only reliable way to ensure the video stops playing in IE

            $("#trailer-video-container").empty();

        });



        // Start playing the video whenever the trailer modal is opened

        $(document).on('click', '.movie-tile', function (event) {

            // Don't display the modal if we're not over the image itself

            var imageData = $(this).children('.image').data('overImage');

            if (imageData === 'no' || imageData === undefined) {

                var myModal = $(document).find('.modal');

                myModal.modal('hide');

                   return false;

            }

            // Otherwise...

            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')

            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId

                    + '?autoplay=1&html5=1';

            $("#trailer-video-container").empty().append(

                    $("<iframe></iframe>", {

                'id': 'trailer-video',

                'type': 'text-html',

                'src': sourceUrl,

                'frameborder': 0

            }));

        });



        // Animate in the movies when the page loads

        $(document).ready(function () {

            $('.movie-tile').hide().first().show("fast", function showNext() {

                $(this).next("div").show("fast", showNext);

            });

        });



    </script>

</head>

'''





# The main page layout and title bar

main_page_content = '''

<body>

    <!-- Trailer Video Modal -->

    <div class="modal" id="trailer">

        <div class="modal-dialog">

            <div class="modal-content">

                <a href="#" class="hanging-close" data-dismiss="modal"

                        aria-hidden="true">

                    <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7\

WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>

                </a>

                <div class="scale-media" id="trailer-video-container">

                </div>

            </div>

        </div>

    </div>



    <!-- Main Page Content -->

    <div class="container">

        <div class="navbar navbar-fixed-top" role="navigation">

            <div class="container">

                <div class="navbar-header">

                    <a class="navbar-brand" href="#">Fresh Tomatoes Movie

                            Trailers

                    </a>

                </div>

            </div>

        </div>

    </div>

    <div class="container">{movie_tiles}</div>

</body>

</html>

'''





# A single movie entry html template

movie_tile_content = '''

<div class="col-md-6 col-lg-4 movie-tile text-center"

        data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal"

        data-target="#trailer">

    <img src="{poster_image_url}" class="image" width="220" height="342">

    <h2 class="title" title="{year}">{movie_title}</h2>

    <p class="plot" id="plot-{trailer_youtube_id}">{movie_plot}</p>

    <table class="table0">

        <tr><td class="data0">{starring[0]}</td></tr>

        <tr><td class="data1">{starring[1]}</td></tr>

        <tr><td class="data2">{starring[2]}</td></tr>

        <tr><td class="data3">{starring[3]}</td></tr>

    </table>

</div>

'''





def create_movie_tiles_content(movies):

    # The HTML content for this section of the page

    content = ''

    for movie in movies:

        # Extract the youtube ID from the url

        youtube_id_match = re.search(

            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)

        youtube_id_match = youtube_id_match or re.search(

            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)

        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match

                              else None)



        # Append the tile for the movie with its content filled in

        content += movie_tile_content.format(

            movie_title=movie.title,

            poster_image_url=movie.poster_image_url,

            trailer_youtube_id=trailer_youtube_id,

            movie_plot=movie.plot,

            year=movie.year,

            starring=movie.starring

        )

    return content





def open_movies_page(movies):

    # Create or overwrite the output file

    output_file = open('fresh_tomatoes.html', 'w')



    # Replace the movie tiles placeholder generated content

    rendered_content = main_page_content.format(

        movie_tiles=create_movie_tiles_content(movies))



    # Output the file

    output_file.write(main_page_head + rendered_content)

    output_file.close()



    # open the output file in the browser (in a new tab, if possible)

    url = os.path.abspath(output_file.name)

    webbrowser.open('file://' + url, new=2)
