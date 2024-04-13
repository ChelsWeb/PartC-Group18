const categorySelect = document.getElementById('category');
const locationInput = document.getElementById('locationInput');
const products = document.querySelectorAll('.post');

categorySelect.addEventListener('change', filterPosts);
locationInput.addEventListener('input', filterPosts);

function filterByLocation() {
    const selectedLocation = locationInput.value.trim().toLowerCase();

    products.forEach(function (product) {
        const productLocation = product.getAttribute('data-location').toLowerCase();

        if (productLocation === selectedLocation) {
            product.style.display = 'inline-block';
        } else {
            product.style.display = 'none';
        }
    });
}

function cancelLocationFilter() {
    locationInput.value = '';
    filterPosts();
}

function filterPosts() {
    const selectedCategory = categorySelect.value.toLowerCase();
    const selectedLocation = locationInput.value.trim().toLowerCase();

    products.forEach(function (product) {
        const productCategory = product.classList[1].toLowerCase(); // Assuming each post has only one category
        const productLocation = product.getAttribute('data-location').toLowerCase();

        if ((selectedCategory === 'all' || productCategory === selectedCategory) &&
            (selectedLocation === '' || productLocation === selectedLocation)) {
            product.style.display = 'inline-block';
        } else {
            product.style.display = 'none';
        }
    });
}

function toggleFavorite(postId, element) {
    const liked = element.querySelector('img').src.includes('liked.png'); // Determine if currently liked or not
    fetch('/toggle-favorite', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({post_id: postId, liked: !liked}),
        credentials: 'same-origin'  // Important for sessions to work
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Toggle the image based on current state
                element.querySelector('img').src = liked ? "{{ url_for('explore.static', filename='like.png') }}" : "{{ url_for('explore.static', filename='liked.png') }}";
            } else {
                alert(data.error || 'An error occurred');
            }
        });
}


