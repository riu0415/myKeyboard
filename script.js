document.getElementById('fileInput').addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = () => {
        main(reader.result.split(/\s+/))
    };

    reader.readAsText(file);
});

function renzoku(data) {
    const keys = {}
    for (let i = 0; i < data.length - 1; i++) {
        if (keys[data[i]] !== undefined) {
            if (keys[data[i]][data[i + 1]] !== undefined) {
                keys[data[i]][data[i + 1]] += 1
            } else {
                keys[data[i]][data[i + 1]] = 1
            }
        } else {
            keys[data[i]] = {}
            keys[data[i]][data[i + 1]] = 1
        }
    }
    console.log(keys)
}