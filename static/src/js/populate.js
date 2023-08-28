// Function to populate the District select element based on selected Province
document.addEventListener("DOMContentLoaded", function () {
    function populateDistricts() {
        const provinceSelect = document.getElementById('perm_province');
        const districtSelect = document.getElementById('perm_district');
        const selectedProvince = provinceSelect.value;

        districtSelect.innerHTML = ''; // Clear existing options

        // Fetch the JSON data from districts.json
        fetch('./districts.json')
            .then(response => response.json())
            .then(data => {
                const province = data.provinces.find(p => p.provienceName === selectedProvince);
                if (province) {
                    province.districtNames.forEach(district => {
                        const option = document.createElement('option');
                        option.value = district.name;
                        option.textContent = district.name;
                        districtSelect.appendChild(option);
                    });
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Function to populate the Municipality select element based on selected District
    function populateMunicipalities() {
        const districtSelect = document.getElementById('perm_district');
        const municipalitySelect = document.getElementById('perm_municipality');
        const selectedDistrict = districtSelect.value;

        municipalitySelect.innerHTML = ''; // Clear existing options

        // Fetch the JSON data from districts.json
        fetch('districts.json')
            .then(response => response.json())
            .then(data => {
                const province = data.provinces.find(p => p.provienceName === 'Koshi'); // Replace with selectedProvince
                if (province) {
                    const district = province.districtNames.find(d => d.name === selectedDistrict);
                    if (district) {
                        district.municipalities.forEach(municipality => {
                            const option = document.createElement('option');
                            option.value = municipality;
                            option.textContent = municipality;
                            municipalitySelect.appendChild(option);
                        });
                    }
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Attach event listeners to Province and District select elements
    document.getElementById('perm_province').addEventListener('change', populateDistricts);
    document.getElementById('perm_district').addEventListener('change', populateMunicipalities);

    // Initial population of District select element
    populateDistricts();
});
