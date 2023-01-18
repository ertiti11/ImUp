import React from 'react'
import { images } from '../../services/GetImages';
import Image from '../Image/Image';
export default function ImageList() {

  return(

<div >
  {
        images.map((image)=>{
          let url = `http://127.0.0.1:8090/api/files/${image.collectionName}/${image.id}/${image.image}`
          return <Image key={image.id} url={url} title={image.title}/>
        })
  }
</div>

  );



  
}

