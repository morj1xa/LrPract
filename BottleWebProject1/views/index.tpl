% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron" style="background-color:#282a36">
    <h1 style="color:white">Boxing Legends</h1>
    <p style="color:white" class="lead">Dive into the legendary world of boxing: stories of the greatest champions, their uncompromising fights, and unmatched skills - all in one place! Experience the thrilling moments of sporting history and discover which legends made boxing unparalleled.</p>
</div>

<div class="row">
    <div class="col-md-4">
        <img src="static/images/floydmayweather2.png" alt="Boxing Legends Image">
        <h2 style="color:white">Floyd Mayweather</h2>
        <p style="color:white">
            Floyd Mayweather is considered one of the greatest boxers of all time because of his fast and destructive combinations, 
            as well as superhuman reflexes. In his first championship in 1998, he defeated Genaro Hernandez in the eighth round, 
            despite his relative inexperience. After defending the title, Mayweather won the WBC lightweight title against Jose Luis Castillo, 
            and then, less than three years later, won the welterweight title with a dominant victory over Arturo Gatti.
        </p>
        <p><a class="btn btn-default" href="https://biographe.ru/sportsmeni/floyd-mayweather/">Find out more information about the fighter &raquo;</a></p>
    </div>
    <div class="col-md-4">
    <img src="static/images/tyson.png">
        <h2 style="color:white">Mike Tyson</h2>
        <p style="color:white">Mike Tyson, born in Brownsville, Brooklyn, has become one of the greatest boxers of recent decades. 
        At the peak of his career, he was the most powerful attacker in the history of boxing. Tyson was a student of Cus 
        D'Amato and under the guidance of trainers such as Kevin Rooney and Teddy Atlas. 
        He became the youngest heavyweight champion by knocking out Trevor Berbick on November 22, 1986. Tyson's success was just a matter of time.
        "Iron Mike" became heavyweight champion in history.</p>
        <p><a class="btn btn-default" href="https://biographe.ru/sportsmeni/maik-taison/">Find out more information about the fighter&raquo;</a></p>
    </div>
    <div class="col-md-4">
    <img src="static/images/ali.png">
        <h2 style="color:white">Muhammad Ali</h2>
        <p style="color:white">Muhammad Ali, the legendary boxer, became a symbol of the fight for justice. His incredible skills and lightning-fast hand speed made him a master in the ring. \
        Starting his career with 19 wins, he shocked the world by defeating Sonny Liston in 1964. Ali defended his title nine times but was temporarily stripped 
        of his license for refusing to participate in the Vietnam War. However, he came back and defeated Jerry Quarry, becoming one of the brightest stars in boxing.</p>
        <p><a class="btn btn-default" href="https://biographe.ru/sportsmeni/muhamed-ali/">Find out more information about the fighter &raquo;</a></p>
    </div>
    <h3 style="color:white"> Ask a Question </h3>
    <form action="/home" method="post">
        <p><textarea rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
        <p><input type="text" size="50" name="USERNAME" placeholder="Your username"></p>
        <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
        <p class="btn btn-default". ><input type="submit" value="Send"></p>
    </form>

</div>
