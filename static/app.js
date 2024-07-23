// the code that makes the animation, would of used python but this is easier 

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {

        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show')
        }



    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));