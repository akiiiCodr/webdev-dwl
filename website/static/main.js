function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main');

    // Toggle sidebar visibility
    if (sidebar.style.left === '0px') {
        sidebar.style.left = '-250px';
        mainContent.classList.remove('active');
    } else {
        sidebar.style.left = '0px';
        mainContent.classList.add('active');
    }
}
    // Notificationo Bell 
    function toggleNotification() {
      const notificationContent = document.getElementById('notificationContent');
      notificationContent.style.display = 
        notificationContent.style.display === 'block' ? 'none' : 'block';
    }

    document.addEventListener('click', function(event) {
      const notificationContent = document.getElementById('notificationContent');
      const bell = document.querySelector('.notification');
      if (!notificationContent.contains(event.target) && !bell.contains(event.target)) {
        notificationContent.style.display = 'none';
      }
    });
 
    // Menu Bar
    function toggleMenu() {
        const dropdown = document.getElementById("dropdownMenu");
        dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
    }
    
    // Close the dropdown if the user clicks outside of it
    window.onclick = function(event) {
        if (!event.target.matches('.menu-button')) {
            const dropdown = document.getElementById("dropdownMenu");
            if (dropdown.style.display === "block") {
                dropdown.style.display = "none";
            }
        }
    }
    
