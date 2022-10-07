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
                    <input type="number" name="add_money"  class="form-control" step="100" required="" id="edit-post-textarea" min="500" max="100000">
                </div>
                <input type="submit" class="btn btn-sm btn-outline-primary" value="Save"/>

            </form>`

            // document.querySelector('#edit-post-form').onsubmit = () => {
            //     // retrieve data entered by the user

            //     // lấy dữ liệu do người dùng nhập vào
            //     const money = document.querySelector('#edit-post-textarea').value;
            //     const user_id = btn.dataset.user_id
            //     // console.log("kldajsdlka")
            //     // const yes = 7

            //     // Send POST request to /emails
            //     // Gửi yêu cầu POST tới / email
            //     fetch('/add_bid', {
            //         method: 'POST',
            //         body: JSON.stringify({money:money, user_id:user_id})
            //     })
            //         .then(response => response.json())
            //         .then(result => {
            //             if (result.error) {
            //                 console.log(`Error editing post: ${result.error}`);
            //             } else {
            //                 console.log(result.message)
            //                 moneyDiv.innerHTML = money
            //                 btn.style.display = 'block'
            //             }
            //         })
            //         .catch(err => {
            //             console.log(err)
            //         })
            //     return false;
            // }

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
                    <input type="number" name="num_date"  class="form-control" step="1" required="" id="edit-post-textarea" min="1" max="90">
                </div>
                <input type="submit" name="change" class="btn btn-sm btn-outline-primary" value="Chốt">

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
