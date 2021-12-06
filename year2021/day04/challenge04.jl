using DelimitedFiles

file = "input04.txt"
blocks = DelimitedFiles.readdlm(file, skipstart=2)
num_blocks = Int(size(blocks, 1) / size(blocks, 2))
block_len = size(blocks, 2)

f = open(file, "r")
    l = readlines(f)
close(f)
rng = split(l[1], ",")

function iswinner(b)
    for row in eachrow(b)
        if count(x->x==1, row) == length(row)
            return true
        end
    end
    for row in eachrow(transpose(b))
        if count(x->x==1, row) == length(row)
            return true
        end
    end
    return false
end

markers = zeros(Int, size(blocks, 1), size(blocks, 2))

function play()
for draw in rng
    for (i, x) in enumerate(blocks)
        row = mod(i, size(blocks, 1))
        if row == 0
            row = size(blocks, 1)
        end
        column = trunc(Int, ((i - 1) / size(blocks, 1))) +1
        #println("row $row")
        #println("column $column")
        #println(x)
        if x == parse(Int, draw)
            markers[row, column] = 1
        end
    end
    for j in range(1, length=num_blocks, step=block_len)
        bl = markers[j:j+4,:]
        if iswinner(bl)
            global winner = j            
            return draw
            #@goto escape_label
        end
    end
end
end

#@label escape_label
last_draw = play()
winning_mask = markers[winner:winner+4,:]
winning_block = blocks[winner:winner+4,:]
println(winning_mask)
println(winning_block)
println("Last number drawn: $last_draw")

winning_sum = 0
for (i, j) in zip(winning_mask, winning_block)
    if i == 0
        global winning_sum += j 
    end
end
println("Winning sum: $winning_sum")
result1 = winning_sum * parse(Int, last_draw)
println("Result part 1: $result1")

markers = zeros(Int, size(blocks, 1), size(blocks, 2))


function play_to_loose()
bingo = []
for draw in rng
    for (i, x) in enumerate(blocks)
        row = mod(i, size(blocks, 1))
        if row == 0
            row = size(blocks, 1)
        end
        column = trunc(Int, ((i - 1) / size(blocks, 1))) +1
        if x == parse(Int, draw)
            markers[row, column] = 1
        end
    end
    for j in range(1, length=num_blocks, step=block_len)
        bl = markers[j:j+4,:]
        if j in bingo
            continue
        elseif iswinner(bl)
            append!(bingo, j) 
            if length(bingo) == num_blocks
                global looser = j
                return draw
            end
        end
    end
end
end

final_draw = play_to_loose()
loosing_mask = markers[looser:looser+4,:]
loosing_block = blocks[looser:looser+4,:]
println("Last number drawn: $final_draw")

loosing_sum = 0
for (i, j) in zip(loosing_mask, loosing_block)
    if i == 0
        global loosing_sum += j 
    end
end
println("Loosing: $loosing_sum")
result2 = loosing_sum * parse(Int, final_draw)
println("Result part 2: $result2")

