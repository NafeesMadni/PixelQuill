function openLogoutModal() {
     document.getElementById('logoutModal').classList.remove('hidden');
}

function closeLogoutModal() {
     document.getElementById('logoutModal').classList.add('hidden');
}

function confirmLogout() {
     // Redirect to the actual logout URL
     window.location.href = "{% url 'authentication:logout' %}";
}