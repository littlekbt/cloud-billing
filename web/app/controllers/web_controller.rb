class WebController < ApplicationController
  include WebControllerHelper

  def index
    now = Date.current
    begin_date = params[:begin_date] || now.to_s
    end_date = params[:end_date] || (now + 7.days).to_s
    # unit_ids = current_user.units.map(&:id)
    @datas = request_billing([1,2], begin_date, end_date)
    p @datas
    # for develop
    # @datas = [JSON.parse(test)]
  end

  private
  def test
    datas = Proc.new{first=0;10.times.map{|_| first += rand(7)}}
    <<EOF
{
	"unitId": 1,
  "startDate": "20170801",
  "endDate": "20170810",
	"resources": [
    {
			"resource": "S3",
			"datas": #{datas.call}
		},
		{
			"resource": "Dynamo",
			"datas": #{datas.call}
		},
		{
			"resource": "lambda",
			"datas": #{datas.call}
		},
		{
			"resource": "EC2",
			"datas": #{datas.call}
		}
	]
}
EOF
  end
end
