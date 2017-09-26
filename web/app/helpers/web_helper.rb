module WebHelper
  def get_max(data)
    max = data['resources'].map{|r|r['datas'].map{|data|data.to_f}}.flatten.max
    max.ceil(-((max.to_i.to_s.size)-1))
  end
end
