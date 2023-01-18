import React from 'react'

export default function Image({url, title}) {
  return (
    <div >
        <img src={url} alt={title} />
        <p>{title}</p>
    </div>

    
  )
}
