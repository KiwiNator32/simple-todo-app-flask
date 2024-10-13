let url = '/tasks'

function task_completed(id) {
    let final_url = url + '/' + id
    if(HttpDelete(final_url)) {
        location.reload()
    }
}

async function HttpDelete(url) {
        try {
          const response = await fetch(url, {
            method: 'DELETE',
          });
      
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
      
          const data = await response.json(); // assuming the response has JSON content
          console.log('Deleted successfully:', data);
        } catch (error) {
          console.error('Error with DELETE request:', error);
        }
}