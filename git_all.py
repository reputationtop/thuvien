…or push an existing repository from the command line
hoặc đẩy một kho lưu trữ hiện có từ dòng lệnh
git remote add origin https://github.com/reputationtop/3yt.git
git branch -M main
git push -u origin main

…or create a new repository on the command line
hoặc tạo một kho lưu trữ mới trên dòng lệnh
echo "# 3yt" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/reputationtop/3yt.git
git push -u origin main



<!DOCTYPE html>
  chúng tôi có thể yêu cầu trình duyệt cung cấp tọa độ GPS của người dùng:
<html lang="en">
    <head>
        <title>geolocation</title>
    </head>
    <body>
        <script>
          
            navigator.geolocation.getCurrentPosition(function(position) {
                document.write(position.coords.latitude + ", " + position.coords.longitude);
            });
  
        </script>
    </body>
</html>


git clone <repository url>. 
    Thao tác này sẽ tải kho lưu trữ xuống máy tính của bạn.

    Run ls, là lệnh liệt kê tất cả các tệp và thư mục trong thư mục hiện tại của bạn. 

    git add <new file name>để theo dõi tệp cụ thể đó hoặc 
        git add .để theo dõi tất cả các tệp trong thư mục đó.   


Sau khi thực hiện một số thay đổi đối với tệp, chúng tôi có thể cam kết những thay đổi đó,
    chụp nhanh trạng thái hiện tại của mã của chúng tôi. chạy: git commit -m "some message"

    chạy git statusđể xem mã của chúng tôi so với mã trên kho lưu trữ từ xa như thế nào

    Khi chúng tôi sẵn sàng xuất bản các cam kết địa phương của mình lên Github
    , chúng tôi có thể chạy git push

    Nếu bạn chỉ thay đổi các tệp hiện có và không tạo tệp mới, thay vì sử dụng 
    git add .và sau đó git commit...
     chúng ta có thể cô đọng điều này thành một lệnh git commit -am "some message" 

chạy git pullđể kéo bất kỳ thay đổi từ xa nào vào kho lưu trữ của bạn.

Một lệnh git có thể hữu ích khác là git log, 
    cung cấp cho bạn lịch sử tất cả các cam kết của bạn trên kho lưu trữ đó.


Có khả năng hữu ích hơn nữa, nếu bạn nhận ra rằng mình đã mắc lỗi,
 bạn có thể hoàn nguyên về cam kết trước đó bằng cách sử dụng lệnh 
git resettheo một trong hai cách:
   1 git reset --hard <commit>hoàn nguyên mã của bạn về chính xác như thế nào sau khi cam kết được chỉ định.
        Để chỉ định cam kết, hãy sử dụng băm cam kết được liên kết với một cam kết có thể được tìm 
        thấy bằng cách sử dụng git lognhư hình trên.
   2 git reset --hard origin/masterhoàn nguyên mã của bạn về phiên bản hiện
    được lưu trữ trực tuyến trên Github.

Chạy git branchđể xem bạn hiện đang làm việc ở chi nhánh nào,
     chi nhánh này sẽ có dấu hoa thị ở bên trái tên của nó.

     Để tạo một chi nhánh mới, chúng tôi sẽ chạy
     git checkout -b <new branch name>

        Chuyển đổi giữa các nhánh bằng lệnh git checkout <branch name>và 
            thực hiện bất kỳ thay đổi nào đối với mỗi nhánh.

            Khi chúng ta đã sẵn sàng hợp nhất hai nhánh của chúng ta lại với nhau,
             chúng ta sẽ kiểm tra nhánh mà chúng ta muốn giữ lại (hầu như luôn là nhánh chính) và sau đó 
             chạy lệnh git merge <other branch name>.
                 Điều này sẽ được xử lý tương tự như đẩy hoặc kéo và xung đột hợp nhất có thể xuất hiện.