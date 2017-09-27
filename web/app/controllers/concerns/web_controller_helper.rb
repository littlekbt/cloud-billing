module WebControllerHelper
  def request_billing(unit_ids, begindate, enddate)
    conn = Faraday.new(:url => 'http://192.168.10.162:8080') do |faraday|
      faraday.request  :url_encoded             # form-encode POST params
      faraday.response :logger                  # log requests to STDOUT
      faraday.adapter  Faraday.default_adapter  # make requests with Net::HTTP
    end
    res = conn.get '/', { :unit_ids => unit_ids.join(','), :begin_date => begindate, :end_date => enddate }
    JSON.parse res.body
  end
end
