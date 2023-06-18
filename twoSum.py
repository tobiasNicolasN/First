def twoSum(nums, target):
    numSum =[]
    for num in nums:
        contador = 0
        while num != nums[contador]:
            if num + nums[contador] == target:
                numSum.append(nums.index(num))
                numSum.append(contador)
                return numSum
            contador += 1
    if len(numSum) < 1:
        return "Ninguna suma da el target buscado."