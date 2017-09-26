class WebController < ApplicationController
  def index
    # @datas = current_user.units.map do |unit|
    #   requestBilling(unit.id, daterange)
    # end

    # for develop
    @datas = [JSON.parse(test)]
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
