 // Fetch testimonials from backend
 fetch('/fetch-testimonials')
 .then(response => response.json())
 .then(testimonials => {
     const swiperWrapper = document.querySelector('.testimonials-slider .swiper-wrapper');

     testimonials.forEach(testimonial => {
         const testimonialItem = `
         <div class="swiper-slide">
             <div class="testimonial-item">
                 <p>
                     <i class="bx bxs-quote-alt-left quote-icon-left"></i>
                     ${testimonial.testimonial_text}
                     <i class="bx bxs-quote-alt-right quote-icon-right"></i>
                 </p>
                 <img src="${testimonial.photo_url}" class="testimonial-img" alt="${testimonial.name}">
                 <h3>${testimonial.name}</h3>
                 <h4>${testimonial.company}</h4>
             </div>
         </div>`;
         swiperWrapper.innerHTML += testimonialItem;
     });

     // Initialize swiper slider after adding testimonials
     new Swiper('.testimonials-slider', {
         // Your swiper configuration options here
     });
 })
 .catch(error => {
     console.error('Error fetching testimonials:', error);
 });
