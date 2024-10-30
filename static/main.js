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