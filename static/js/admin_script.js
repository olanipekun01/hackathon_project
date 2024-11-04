let btn = document.querySelector('#btn');
        let sidebar = document.querySelector('.sidebar');
        let searchBtn = document.querySelector('.bx-search');

        


        function handleResultModal(link, code) {
            document.querySelector(".upload_result").style.display = "block";
            document.querySelector(".background_wrapper").style.display = "block";
        }

        function closeResultModal() {
            event.preventDefault();
            document.querySelector(".upload_result").style.display = "none";
            document.querySelector(".background_wrapper").style.display = "none";
        }

        function handleGrade(link, code) {
            document.querySelector(".update_grade").style.display = "block";
            document.querySelector(".background_wrapper").style.display = "block";
        }

        function closeGradeModal() {
            event.preventDefault();
            document.querySelector(".update_grade").style.display = "none";
            document.querySelector(".background_wrapper").style.display = "none";
        }

        function handleCreateModal() {
            document.querySelector(".create_programme").style.display = "block";
            document.querySelector(".background_wrapper").style.display = "block";
        }

        function closeCreateModal() {
            event.preventDefault();
            document.querySelector(".create_programme").style.display = "none";
            document.querySelector(".background_wrapper").style.display = "none";
        }

        function handleUpdateModal() {
            document.querySelector(".update_programme").style.display = "block";
            document.querySelector(".background_wrapper").style.display = "block";
        }

        function closeUpdateModal() {
            event.preventDefault();
            document.querySelector(".update_programme").style.display = "none";
            document.querySelector(".background_wrapper").style.display = "none";
        }


        function showFilterModal() {
            // document.querySelector(".issue_modal_container").style.display = "block";
            document.querySelector(".filter_container").style.display = "block";
        };

        function closeFilterModal() {
            event.preventDefault();
            document.querySelector(".filter_container").style.display = "none";
            // document.querySelector(".background_wrapper").style.display = "none";
        }

        // document.getElementById("cancelBtn").addEventListener("click", function (event) {
        //     event.preventDefault();
        //     document.querySelector(".modal_container").style.display = "none";
        // })


        function handleDeletePopOut(link, name) {
            document.querySelector(".deletePopOut").style.display = "block";
            document.querySelector(".background_wrapper").style.display = "block";
            document.querySelector(".popOutItemLink").href = link;
            document.querySelector(".popOutItemName").innerHTML = name;
        }


        function closePopOut() {
            event.preventDefault();
            document.querySelector(".deletePopOut").style.display = "none";
            document.querySelector(".background_wrapper").style.display = "none";
        }



        btn.onclick = function () {
            sidebar.classList.toggle("active");
        }

        searchBtn.onclick = function () {
            sidebar.classList.toggle("active");
        }