import React from 'react';

export const Carousel = ({ images }) => {
  return (
    <div className="carousel">
      {images.map((image, index) => (
        <div key={index} className="carousel-item">
          <img src={image} alt={`Slide ${index}`} />
        </div>
      ))}
    </div>
  );
};

