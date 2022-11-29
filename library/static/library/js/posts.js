document.addEventListener('DOMContentLoaded', function() {

    // nap tien
  document.querySelectorAll('.editmoney').forEach(btn => {
    btn.onclick = function () {
        
        btn.style.display = 'none'
        console.log(btn.dataset.userid)
    
        let moneyDiv = document.querySelector(`#money${btn.dataset.userid}`);
        var nowmoney = moneyDiv.innerHTML
        moneyDiv.innerHTML =
        // ` <form id="edit-post-form" action="/add_bid/${btn.dataset.userid}" method="POST" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">
        ` <form id="edit-money-form" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem ;min-width:150px;">
            <div>
                <input null="false"  type="number" placeholder="Nhập số tiền nạp thêm" class="form-control" step="1000" required="" id="edit-money-textarea" min="5000" max="500000">
            </div>
            <input name="nap" type="submit" class="btn btn-sm btn-outline-secondary" value="nạp"/>
            <input name="rut" type="submit" class="btn btn-sm btn-outline-secondary" value="Rút"/>
            <input name="close" type="submit" class="btn btn-sm btn-outline-secondary" value="&#9746;"/>

        </form>`


        $('input[name=close]').click(function (e) {

          moneyDiv.innerHTML = nowmoney
          btn.style.display = 'block'
          return false;
        });



        $('input[name=nap]').click(function (e) {
          // alert('bnap' + nowmoney );
          const money_if = document.querySelector('#edit-money-textarea').value;
          const user_id = btn.dataset.userid;
          var money_after =  parseInt(nowmoney) + parseInt(money_if) ;
          var money_after =  parseInt(nowmoney, 10) + parseInt(money_if, 10) ;
          if(money_if == "" || money_if == null || parseInt(money_if) < 5000){
            alert("Error");
            return false;
          }
          confirm('Xác nhận nạp' + money_if+ "vnd")
          fetch('/add_bid', {
            method: 'PUT',
            
            body : JSON.stringify({addmoney: true,money_if,user_id})
          })
              .then(response => response.json())
              
              .then(result => {
                  if (result.error) {
                      console.log(`Lỗi khi nạp tiền: ${result.error}`);
                  } else {
                      console.log(result.message)
                      moneyDiv.innerHTML = money_after
                      btn.style.display = 'block'
                  }
              })
              .catch(err => {
                  console.log(err)
              })
          return false;
        });

        $('input[name=rut]').click(function (e) {
    
          const money_if = document.querySelector('#edit-money-textarea').value;
          var money_after =  parseInt(nowmoney) - parseInt(money_if) ;
          // var money_after =  parseInt(nowmoney, 10) + parseInt(money_if, 10) ;
          const user_id = btn.dataset.userid;
          if(money_if == "" || money_if == null || parseInt(money_if) < 5000|| parseInt(money_if) > 500000){
            alert("Bạn phải nhập số");
            return false;
          }
          confirm('Xác nhận rút' + money_if+ "vnd")
          if ( parseInt(money_after) < 0 ) {
            alert('Không thể rút quá số tiền đang có '+ parseInt(nowmoney));
            return false;
          } else {
              fetch('/add_bid', {
                method: 'PUT',
                // name: "CS Lewis",
                body: JSON.stringify({ money_if, user_id })
            })
                .then(response => response.json())
                .then(result => {
                    if (result.error) {
                        console.log(`Lỗi khi rut tiền: ${result.error}`);
                    } else {
                        console.log(result.message)
                        moneyDiv.innerHTML = money_after
                        btn.style.display = 'block'
                    }
                })
                .catch(err => {
                    console.log(err)
                })
                
          }
          return false;
        });

        

      }
  })
  // thêm thể loại mới
  document.querySelectorAll('.editcategory').forEach(btn => {
    btn.onclick = function () {
        btn.style.display = 'none'
        console.log(btn.dataset.userid)
        let moneyDiv = document.querySelector(`#edit_category`)
        moneyDiv.innerHTML =
        ` <form  action="/newcategory" method="POST" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">
            <div>

              Nhập:<input maxlength= "25" type="text" name="new_category" placeholder="Nhập tên thể loại cần thêm" class="form-control"  required=""   >
            </div>
            <input type="submit" class="btn btn-sm btn-outline-primary" value="Lưu"/>

        </form>`


    }
  })
  // xác nhận việc mượn sách chủa hs/cho mượn
  document.querySelectorAll('.editlisting').forEach(btn => {
      btn.onclick = function () {
          btn.style.display = 'none'
          console.log(btn.dataset.listid)
          let listDiv = document.querySelector(`#list${btn.dataset.listid}`)
          var listup = listDiv;
          listDiv.innerHTML =
          ` <form id="edit-listing-form" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">

              <div>
                  <input type="number" placeholder="Nhập số ngày" class="form-control" step="1" required="" id="edit-listing-textarea" min="1" max="90">
              </div>
              <input name="change" type="submit"  class="btn btn-sm btn-outline-secondary" value="xác nhận">
              <input name="close" type="submit" class="btn btn-sm btn-outline-secondary" value="&#9746;"/>
          </form>`


          $('input[name=close]').click(function (e) {

            listDiv.innerHTML = listup
            btn.style.display = 'block'
            return false;
          });

          $('input[name=change]').click(function (e) {
    
            const date_if = document.querySelector('#edit-listing-textarea').value;
            const listing_id = btn.dataset.listid;
            if(date_if == "" || date_if == null || parseInt(date_if) < 0 || parseInt(date_if) > 90){
              alert("Error");
              return false;
            }
            confirm('Xác nhận cho mượn' + date_if+ " ngày?")
                fetch('/change_listing', {
                  method: 'PUT',
                  body: JSON.stringify({ date_if, listing_id })
              })
                .then(response => response.json())
                .then(result => {
                    if (result.error) {
                        console.log(`Lỗi khi rut tiền: ${result.error}`);
                    } else {
                      window.location.reload();
                    }
                })
                .catch(err => {
                    console.log(err)
                })
            return false;   
            
            
          });
  
  



      }
  })
  // kết thúc phiên mượn sách của học sinh
  document.querySelectorAll('.close-book').forEach(btn => {
    btn.onclick = function () {
      confirm("kết thúc danh sách")
      // alert("kết thúc danh sách");
      fetch('/close_listing', {
        method:'PUT',
        body: JSON.stringify({list_id:btn.dataset.listid})
      })
      
        .then(response => response.json())
        .then(result => {
          if (result.error) {
              console.log(`loi : ${result.error}`);
          } else {
            window.location.reload();
          }
        })
    }
  })



  // liwowtj thích/không
  document.querySelectorAll('.like-book').forEach(btn => {
    btn.onclick = function () {
      var name_buton = btn.name
      alert("tên nút " + name_buton);
      fetch('/changebook', {
        method:'PUT',
        body: JSON.stringify({likebook: true,bookid:btn.dataset.bookid})
      })
      
        .then(response => response.json())
        .then(result => {
          if (result.error) {
              console.log(`loi : ${result.error}`);
          } else {
            window.location.reload();
          }
        })
    }
  })

  document.querySelectorAll('.edit_num_book').forEach(btn => {
    btn.onclick = function () {
        btn.style.display = 'none'
        console.log(btn.dataset.listid)
        let listDiv = document.querySelector(`#list${btn.dataset.listid}`)
        listDiv.innerHTML =
        ` <form id="edit-post-form" action="/change_listing/${btn.dataset.listid}" method="POST" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">

            <div>
                <input type="number" name="num_book" placeholder="Nhập sách" class="form-control" step="1" required="" id="edit-post-textarea" min="1" max="90">
            </div>
            <input type="submit" name="more_book" class="btn btn-sm btn-outline-primary" value="Thêm sách">
            <input type="submit" name="lose_book" class="btn btn-sm btn-outline-primary" value="Loại bớt">

        </form>`
    }
  })







  // chỉnh số lượng sách
  document.querySelectorAll('.editofbook').forEach(btn => {
    btn.onclick = function () {
        btn.style.display = 'none'
        console.log(btn.dataset.listid)
        let listDiv = document.querySelector(`#list${btn.dataset.listid}`)
        listDiv.innerHTML =
        ` <form id="edit-post-form" action="/change_listing/${btn.dataset.listid}" method="POST" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">

            <div>
                <input type="number" name="num_book" placeholder="Nhập sách" class="form-control" step="1" required="" id="edit-post-textarea" min="1" max="90">
            </div>
            <input type="submit" name="more_book" class="btn btn-sm btn-outline-primary" value="Thêm sách">
            <input type="submit" name="lose_book" class="btn btn-sm btn-outline-primary" value="Loại bớt">

        </form>`
    }
  })

  $(document).ready(function() {
      var owl = $('.owl-carousel');
      owl.owlCarousel({
        margin: 10,
        nav: true,
        loop: true,
        responsive: {
          0: {
            items: 1
          },
          600: {
            items: 3
          },
          1000: {
            items: 5
          }
        }
      })
    })

});

