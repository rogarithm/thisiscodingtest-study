def reconstruct_queue(people)
  people.sort!{|a,b| a[0] == b[0] ? a[1] - b[1] : b[0] - a[0]}
  answer = []
  people.each do |person|
    answer.insert(person[1], person)
  end
  answer
end

p reconstruct_queue [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]