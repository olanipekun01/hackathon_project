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

        function handleUpdateModal(name, duration, degree, id) {
            document.querySelector(".update_programme").style.display = "block";
            document.querySelector(".background_wrapper").style.display = "block";
            document.querySelector('#updateModalDegreeInput').value = degree;
            document.querySelector('#updateModalDurationInput').value = duration;
            document.querySelector('#updateModalNameInput').value = name;  
            document.querySelector('#updateModalIdInput').value = id;
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

        function handleCourseUpdateModal(title, code, unit, status, semester, level) {
            document.querySelector(".update_programme").style.display = "block";
            document.querySelector(".background_wrapper").style.display = "block";
            document.querySelector('#updateCourseTitleInput').value = title;
            document.querySelector('#updateCourseCodeInput').value = code;
            document.querySelector('#updateCourseUnitInput').value = unit;  
            document.querySelector('#updateCourseStatusInput').value = status;  
            document.querySelector('#updateCourseSemesterInput').value = semester;
            document.querySelector('#updateCourseLevelInput').value = level; 
            document.querySelector('#updateCourseIdInput').value = id;
        }

        function closeCourseUpdateModal() {
            event.preventDefault();
            document.querySelector(".update_programme").style.display = "none";
            document.querySelector(".background_wrapper").style.display = "none";
        }