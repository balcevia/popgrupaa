import React from 'react';
import Button from '@material-ui/core/Button';

const MyButton = ({onClick, label, ...other}) => {
  return (
    <Button variant="contained" color="primary" onClick={onClick} {...other}>
      {label}
    </Button>
  )
};

export default MyButton;