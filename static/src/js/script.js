// Preview image of the profile photo
document.addEventListener("DOMContentLoaded", function () {
    function displayPreview(event) {
      const previewImage = document.getElementById('imagePreview');
      const photo_label = document.getElementById('photo_label');

      const selectedFile = event.target.files[0];

      if (selectedFile) {
        const imageUrl = URL.createObjectURL(selectedFile);
        previewImage.style.backgroundImage = `url(${imageUrl})`;
        photo_label.style.display = 'none';
      } else {
        previewImage.style.backgroundImage = 'none';
      }
    }
    document.getElementById('photo').addEventListener('change', displayPreview);

    // Default email address
//    function emaildefault() {
//      document.getElementById('email').defaultValue = 'abc@gmail.com';
//    }
//    emaildefault();

    // Language toggle function
    const languageToggle = document.getElementById('language-toggle');
    const nepaliLabel_h1 = document.getElementById('nepali-label-h1');
    const englishLabel_h1 = document.getElementById('english-label-h1');
    const nepaliLabels = document.querySelectorAll('.nepali-label');
    const englishLabels = document.querySelectorAll('.english-label');
    const languageImage = document.getElementById('languageImage');

    languageToggle.addEventListener('change', () => {
      if (languageToggle.checked) {
        languageImage.src = '/raprapa/static/src/img/english.png';
        englishLabels.forEach((label) => (label.style.display = 'inline'));
        nepaliLabels.forEach((label) => (label.style.display = 'none'));
        englishLabel_h1.style.display = 'block';
        nepaliLabel_h1.style.display = 'none';
      } else {
        languageImage.src = '/raprapa/static/src/img/nepal.png';
        englishLabels.forEach((label) => (label.style.display = 'none'));
        nepaliLabels.forEach((label) => (label.style.display = 'inline'));
        nepaliLabel_h1.style.display = 'block';
        englishLabel_h1.style.display = 'none';
      }
    });
});








