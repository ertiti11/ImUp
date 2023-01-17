import React from 'react'

export default function ImageList() {
    images.map((image)=>{
        console.log(image.collectionId)
        console.log(image.id);
        console.log(image.image)
        let images = `http://127.0.0.1:8090/api/files/q9ej2c1xv3v7mhv/${image.id}/${image.image}`
        return <img src={images} alt="" />
      })
  return (
    <div>ImageList</div>
  )
}

s