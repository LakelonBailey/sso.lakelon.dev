import React from 'react';
import { useParams } from 'react-router-dom';

const errorCodeTextMapper = {
  '500': 'Server Error',
  '400': 'Bad Request',
  '401': 'Unauthorized',
  '402': 'Payment Required',
  '403': 'Forbidden',
  '404': 'Not Found',
}

function Error() {
  const { errorCode } = useParams();

  return (
    <div className="bg-slate-900 flex justify-center items-center flex-col h-screen font-mono text-gray-300">
        <h1 className='text-8xl'>{errorCode}</h1>
        <h2 className='text-4xl'>{errorCodeTextMapper[errorCode]}</h2>
    </div>
  );
}

export default Error;
