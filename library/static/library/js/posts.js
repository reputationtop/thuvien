document.addEventListener('DOMContentLoaded', function() {

    // nap tien
  document.querySelectorAll('.edit').forEach(btn => {
      btn.onclick = function () {
          btn.style.display = 'none'
          console.log(btn.dataset.userid)
          let moneyDiv = document.querySelector(`#money${btn.dataset.userid}`)
          moneyDiv.innerHTML =
          // ` <form id="edit-post-form" action="/add_bid/${btn.dataset.userid}" method="POST" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">
          ` <form  action="/add_bid/${btn.dataset.userid}" method="POST" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">
              <div>
                  <input type="number" name="add_money" placeholder="Nhập số tiền nạp thêm" class="form-control" step="100" required="" id="edit-post-textarea" min="500" max="100000">
              </div>
              <input type="submit" class="btn btn-sm btn-outline-primary" value="nạp"/>

          </form>`


      }
  })

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
  document.querySelectorAll('.edit_change').forEach(btn => {
      btn.onclick = function () {
          btn.style.display = 'none'
          console.log(btn.dataset.listid)
          let listDiv = document.querySelector(`#list${btn.dataset.listid}`)
          listDiv.innerHTML =
          ` <form id="edit-post-form" action="/change_listing/${btn.dataset.listid}" method="POST" class="card-text" style="margin-top: 1rem; margin-bottom: 1.6rem">

              <div>
                  <input type="number" name="num_date" placeholder="Nhập số ngày" class="form-control" step="1" required="" id="edit-post-textarea" min="1" max="90">
              </div>
              <input type="submit" name="change" class="btn btn-sm btn-outline-primary" value="Chốt">

          </form>`
      }
  })


  document.querySelectorAll('.close-book').forEach(btn => {
    btn.onclick = function () {
      alert("kết thúc danh sách");
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

