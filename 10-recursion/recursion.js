function addOne(num) {

    if (num >= 9) {
        return num + 1
    }

    total = num + 1
    console.log(total)

    return addOne(total)
}

console.log(addOne(0))

// behaves very similarly! How cool.