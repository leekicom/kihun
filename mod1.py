html1 = """
    <table class="table_col" align="center">
	<tdead>
		<tr>
			<td rowspan="2" scope="col">구분</td>
			<td colspan="4" scope="col" align="center">1차 평가</td>
			<td scope="col" align="center">2차 평가</td>
			<td rowspan="2" scope="col" align="center">계</td>
		</tr>
		<tr>
			<td scope="col">기술자격·면허</td>
			<td scope="col">전공학과</td>
			<td scope="col">출결상황</td>
			<td scope="col">가산점</td>
			<td scope="col" align="center">면접</td>
		</tr>
	</tdead>
	<tbody class="text_center">
		<tr>
			<td scope="row">배점</td>
			<td align="center">50</td>
			<td align="center">40</td>
			<td align="center">10</td>
			<td align="center">15</td>
			<td>적격/부적격</td>
			<td>115</td>
		</tr>
	</tbody>
</table>
"""
html2="""<table class="table_col" align="center">
	<caption></caption>
	<tdead>
		<tr align="center">
			<td scope="col">자격증 명칭</td>
			<td scope="col">자격등급</td>
			<td scope="col">직접관련</td>
			<td scope="col">간접관련</td>
		</tr>
	</tdead>
	<tbody class="text_center" align="center">
		<tr>
			<td rowspan="3" scope="row">국가기술자격증</td>
			<td>기사이상</td>
			<td>50</td>
			<td>40</td>
		</tr>
		<tr>
			<td>산업기사</td>
			<td>45</td>
			<td>35</td>
		</tr>
		<tr>
			<td>기능사</td>
			<td>40</td>
			<td>30</td>
		</tr>
		<tr>
			<td rowspan="3" scope="row">일학습병행자격증<br>
			('22.6.29.부터 적용)</td>
			<td>L6, L5</td>
			<td>50</td>
			<td>40</td>
		</tr>
		<tr>
			<td>L4, L3</td>
			<td>45</td>
			<td>35</td>
		</tr>
		<tr>
			<td>L2</td>
			<td>40</td>
			<td>30</td>
		</tr>
		<tr>
			<td rowspan="2" scope="row">일반자격증</td>
			<td>공 인</td>
			<td>30</td>
			<td rowspan="2">25</td>
		</tr>
		<tr>
			<td>일 반</td>
			<td>26</td>
		</tr>
		<tr>
			<td colspan="2" rowspan="1" scope="row">각종 차량 운전면허증</td>
			<td colspan="2" rowspan="1">90 *운전병에 한함</td>
		</tr>
		<tr>
			<td colspan="2" rowspan="1" scope="row">자격증 미소지</td>
			<td colspan="2" rowspan="1">20</td>
		</tr>
	</tbody>
</table>"""
html3="""<table class="table_col" align="center">
	<tdead align="center">
		<tr>
			<td colspan="2" rowspan="2" scope="col">구분</td>
			<td colspan="2" scope="col">4학년</td>
			<td colspan="2" scope="col">3학년</td>
			<td colspan="2" scope="col">2학년</td>
			<td colspan="2" scope="col">1학년</td>
			<td rowspan="2" scope="col">비전공<br>
			/고퇴이하</td>
		</tr>
		<tr>
			<td scope="col">수료이상</td>
			<td scope="col">재학</td>
			<td scope="col">수료</td>
			<td scope="col">재학</td>
			<td scope="col">수료</td>
			<td scope="col">재학</td>
			<td scope="col">수료</td>
			<td scope="col">재학</td>
		</tr>
	</tdead>
	<tbody class="text_center" align="center">
		<tr>
			<td colspan="2" scope="row">대학교</td>
			<td>40</td>
			<td>38</td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
			<td>28</td>
			<td>26</td>
			<td rowspan="3">20</td>
		</tr>
		<tr>
			<td rowspan="2" scope="rowgroup">전문대</td>
			<td scope="row">3년</td>
			<td>-</td>
			<td>-</td>
			<td>40</td>
			<td>38</td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
		</tr>
		<tr>
			<td scope="row">2년</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
		</tr>
		<tr>
			<td colspan="2" scope="row">고졸</td>
			<td class="text_left" colspan="9">- 전공 34점<span style="color: rgb(0, 0, 205);">, </span>비전공 20점</td>
		</tr>
		<tr>
			<td colspan="2" scope="row">한국폴리텍대학<br>
			인력개발원</td>
			<td class="text_left" colspan="9">- 2년 이상 수료 : 32점<br>
			- 1년 이상 수료 : 30점<br>
			- 6개월 이상 수료 : 26점</td>
		</tr>
	</tbody>
</table><br>
<table class="table_col" align="center">
    <tbody class="text_center" align="center">
		<tr>
			<td rowspan="6">학 점<br>은행제</td>
			<td rowspan="2">학력인정<br>기준학점</td>
			<td colspan="3">배 점</td>
			<td rowspan="2">비고<br>(대학<br>학년)</td>
		</tr>
		<tr>
			<td>학사</td>
			<td>전문학사<br>(3년)</td>
			<td>전문학사<br>(2년)</td>
		</tr>
		<tr>
			<td >40학점 이상</td>
			<td >28</td>
			<td >32</td>
			<td >32</td>
			<td >1학년</td>
		</tr>
		<tr>
			<td >80학점 이상</td>
			<td >32</td>
			<td >36</td>
			<td >36</td>
			<td >2학년</td>
		</tr>
		<tr>
			<td >120학점 이상</td>
			<td >36</td>
			<td >40</td>
			<td ></td>
			<td >3학년</td>
		</tr>
		<tr>
			<td >140학점 이상</td>
			<td >40</td>
			<td ></td>
			<td ></td>
			<td >4학년</td>
		</tr>
    </tbody>
</table>"""
html4="""<table class="table_col" align="center">
	<thead align="center">
		<tr>
			<th scope="col">구분</th>
			<th colspan="5" scope="col">결석일자</th>
			<th scope="col">비고</th>
		</tr>
	</thead>
	<tbody class="text_center" align="center">
		<tr>
			<th scope="row">일수</th>
			<td>0일</td>
			<td>1～2일</td>
			<td>3～4일</td>
			<td>5～6일</td>
			<td>7일 이상</td>
			<td class="text_left" rowspan="2">중학교 또는 고등학교 3년간 결석한 누계 적용</td>
		</tr>
		<tr>
			<th scope="row">배점</th>
			<td>10</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
			<td>6</td>
		</tr>
	</tbody>
</table>
<ul class="list">
	<li>검정고시 합격자/외국의 초.중.고 학력자/초등학교 이하 학력자 : 동일부대·특기 지원자의 평균점수 적용
	<ul>
		<li>(1차 선발 시 지원자의 평균점수, 최종선발 시 1차 선발자의 평균점수 적용, 모병시스템에&nbsp;자동 반영)</li>
	</ul>
	</li>
	<li>지각/조퇴 2회는 결석 1일로 처리</li>
	<li>결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</li>
	<li>결석일 누계 적용 시 소수점 이하는 생략(질병에 의한 결석, 결과, 지각은 적용하지 않음)</li>
	<li>생활기록부 미제출자는 6점부여</li>
</ul>"""
html5="""<ul class="list">
	<li>모집특기 경력 : 6월 ~1년 미만 1점, 1년 ~ 2년 미만 2점, 2년 이상 3점
	<ul>
		<li>모집특기 관련 근무경력자(법인 발행 재직증명서)</li>
		<li>법인체 외 근무자(개인업체) : 모집특기 경력 기간의 1/2 적용</li>
	</ul>
	</li>
	<li>병역진로설계 온라인서비스 군 추천특기 지원자 : 1점
	<ul>
		<li>직업선호도 검사 후 군 특기 추천, 추천 특기로 모집병 지원 시 가산점 부여</li>
	</ul>
	</li>
	<li>독립유공자 손·자녀 또는 국가유공자 자녀 : 4점
	<ul>
		<li><span style="color: rgb(0, 0, 255);">가산점부여 비대상 :&nbsp;지원대상자(유족)확인원 / 5.18민주유공자(유족)확인원 / 특수임무공로자</span></li>
	</ul>
	</li>
	<li>다자녀(3) 가정 자녀 : 4점</li>
	<li>다자녀(2) 가정 자녀 : 2점</li>
	<li>국민기초생활보장법 제7조제1항제1호에 따른 생계급여 수급권자 : 4점</li>
	<li>최근 1년 이내 사회봉사활동 경력 등 : 8점 이내</li>
	<li><span style="color: rgb(0, 0, 255);">헌혈,&nbsp;봉사 통합하여 최대 8점 이내(헌혈, 봉사&nbsp;각각&nbsp;적용 또는 헌혈+봉사 혼합 적용 가능)</span></li>
	<li>
	<table class="table_row" style="width: 500px;">
		<caption>헌혈 배점에대한 설명표이며 헌혈(회수), 봉사(시간)에 대한내용을 제공</caption>
		<tbody>
			<tr>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">배&nbsp; 점</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">1점</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">2점</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">3점</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">4점</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">5점</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">6점</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">7점</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">8점</span></td>
			</tr>
			<tr>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">헌혈(회수)</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">1회</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">2회</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">3회</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">4회</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">5회</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">6회</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">7회</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">8회 이상</span></td>
			</tr>
			<tr>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">봉사(시간)</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">8~15<br>
				시간</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">16~23<br>
				시간</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">24~31<br>
				시간</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">32~39<br>
				시간</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">40~47<br>
				시간</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">48~55<br>
				시간</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">56~63<br>
				시간</span></td>
				<td style="text-align: center;"><span style="color: rgb(0, 0, 0);">64시간<br>
				이상</span></td>
			</tr>
		</tbody>
	</table>
	</li>
	<li><!--StartFragment-->
	<p class="바탕글"><span style="color: rgb(0, 0, 205);"><strong><span style="font-family: 바탕;">※ 헌혈은 헌혈로만&nbsp;점수를 부여하며, 사회봉사 시간으로&nbsp;점수 부여를 하지 않습니다.</span></strong></span></p>
	</li>
	<li>질병치료에 따른 병역처분변경으로 현역병입영대상 판정자 : 4점</li>
</ul>"""
html6="""<a href="https://mma.go.kr/conscription/recruit_service/procedure/army/S_board_text.do?mc=mma0000388&gun_gbcd=1&mojip_gbcd=1" target="_blank">군사특기임무 및 설명</a>"""
html7="""<div class="layout_h4">
<h4>&nbsp;일반기술병(일반직종)</h4>

<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="3" scope="col">서류전형(1차)</th>
			<th rowspan="2" scope="col">면접<br>
			(2차)</th>
			<th rowspan="2" scope="col">계</th>
		</tr>
		<tr>
			<th scope="col">자격/면허&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
			<th scope="col">출결</th>
			<th scope="col">가산점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>70</td>
			<td>20</td>
			<td>15</td>
			<td>35</td>
			<td>140</td>
		</tr>
	</tbody>
</table>
</div>"""
html8="""<div class="layout_h4">
<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="row">구분</th>
			<th colspan="3" scope="col">국가기술자격증</th>
			<th colspan="3" scope="col">일학습병행 자격증</th>
			<th colspan="2" scope="col">일반자격증</th>
			<th rowspan="2" scope="col">미소지</th>
		</tr>
		<tr>
			<th scope="col">기사 이상</th>
			<th scope="col">산업기사</th>
			<th scope="col">기능사</th>
			<th scope="col">L6, L5</th>
			<th scope="col">L4, L3</th>
			<th scope="col">L2</th>
			<th scope="col">공인</th>
			<th scope="col">비공인</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">70</td>
			<td style="text-align: center;">68</td>
			<td style="text-align: center;">66</td>
			<td style="text-align: center;">70</td>
			<td style="text-align: center;">68</td>
			<td style="text-align: center;">66</td>
			<td style="text-align: center;">64</td>
			<td style="text-align: center;">62</td>
			<td style="text-align: center;">60</td>
		</tr>
	</tbody>
</table>
</div>"""
html9="""<div class="layout_h4">
<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="5" scope="col">결석일자</th>
			<th rowspan="2" scope="col">비고</th>
		</tr>
		<tr>
			<th scope="col">0일</th>
			<th scope="col">1~2일</th>
			<th scope="col">3~4일</th>
			<th scope="col">5~6일</th>
			<th scope="col">7일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>20</td>
			<td>19</td>
			<td>18</td>
			<td>17</td>
			<td>16</td>
			<td>고교3년간 누계적용</td>
		</tr>
	</tbody>
</table>
</div>"""
html10="""<div class="layout_h3">
<h3>가산점 : 배점15점</h3>

<ul class="list">
	<li>국가 유공자 자녀, 독립유공자 자녀/손자녀 가산점 : 4점</li>
	<li>질병치유 자진입대 가산점 : 4점
	<ul>
		<li><strong><span style="color: rgb(0, 0, 205);">전시근로역에서 현역병입영대상으로 역종이 변경된 사람.&nbsp; 다만, 보충역은 2021년 10월 13일 이전에 현역병 입영대상으로 역종이 변경된 사람에 한하여 인정</span></strong></li>
	</ul>
	</li>
	<li>국외이주자 중 현역복무지원자 가산점 : 4점
	<ul>
		<li>국외이주자 인정조건(영주권자, 복수국적자, 재외국민 등)과 제출서류 안내는 병적을 관리하는 지방병무청 국외이주 업무담당에게 문의하시기 바랍니다.</li>
	</ul>
	</li>
	<li>다자녀(3명 이상) 가정자녀 가산점 : 4점 /<strong><span style="color: rgb(0, 0, 205);"> 다자녀(2인) 가정자녀 : 2점 </span></strong></li>
	<li>경제적 약자 지원대상(생계급여 수급자) : 4점</li>
	<li>사회봉사활동 경력(접수마감일 기준 최근 1년 이내) :&nbsp;최대8점 (헌혈과 봉사실적을 통합운영)
	<ul>
		<li>사회봉사 : 8시간 이상 1점/ 16시간&nbsp;이상 2점/ 24시간 이상 3점/ 32시간 이상 4점/40시간 이상 5점/48시간 이상 6점/ 56시간 이상 7점/ 64시간 이상 8점</li>
		<li>헌혈 : 1회 1점/ 2회 2점/ 3회 3점/ 4회 4점/ 5회 5점/ 6회 6점/ 7회 7점 /8회 8점
		<ul>
			<li>사회봉사활동 및 헌혈 경력은 회차별 지원서 마감일을 기준으로 기간산정</li>
			<li><strong><span style="color: rgb(0, 0, 255);">헌혈은 헌혈 점수를 부여하며, 사회봉사시간으로 점수부여를 하지 않습니다</span></strong>.<strong><span style="color: rgb(0, 0, 205);"> (중복 불가)</span></strong></li>
			<li>사회봉사활동 경력은 '사회복지사업법'&nbsp;또는 "자원봉사활동기본법' 또는 '청소년활동진흥법'에서 수요처로 지정된 기관에서 실시한 봉사활동만 인정되며, '사회복지 자원봉사 인증관리(VMS) 홈페이지'&nbsp;또는 '1365자원봉사포털'&nbsp;또는&nbsp;'청소년자원봉사포털(DOVOL)'에서 발급하는 봉사활동 증명서로 확인</li>
		</ul>
		</li>
	</ul>
	</li>
	<li>지정특기(방공포, 군사경찰, 조리) 가산점 : 4점
	<ul>
		<li>일반 직종 지원자 중&nbsp;방공포, 군사경찰, 조리 특기 희망자</li>
	</ul>
	</li>
	<li>화생방 직종(운전면허소지자-2종보통이상<strong><span style="color: rgb(0, 0, 205);">(오토제외</span></strong>)) 가산점 : 4점</li>
	<li>항공정비사(기사급) 또는 항공정비 기초인력 인증서 소지자 : 4점
	<ul>
		<li>기계직종(항공기기체정비, 항공기기관정비 특기 희망자) 지원자 중 항공정비사 또는 항공정비 기초인력 인증서 소지자</li>
		<li>통신전자전기직종(항공전자장비정비 특기 희망자) 지원자 중 항공정비사 또는 항공정비 기초인력 인증서 소지자</li>
		<li>항공정비사 자격증에<strong><span style="color: rgb(0, 0, 255);"> FAA A&amp;P (미항공연방청 항공정비사 자격증) 인정</span></strong></li>
	</ul>
	</li>
	<li>병역진로설계 군 추천특기 지원자 가산점 : 1점
	<ul>
		<li><strong><span style="color: rgb(0, 0, 255);">추천받은 특기와 모집병 지원 특기 일치시 가산점 부여</span></strong>(지원서 접수 마감일 기준 최종 직업선호도 검사 결과,</li>
		<li>추천받은특기가 적용되며, 추천특기와 1차 선발 특기가 일치하는 경우 적용 됨)</li>
	</ul>
	</li>
	<li>한국사능력검정(접수마감일 기준 최근 4년 이내, 국사편찬위원회) : 2점
	<ul>
		<li>3, 4급 1점/ 1, 2급 2점</li>
	</ul>
	</li>
	<li>한국어능력검정(접수마감일 기준&nbsp;최근 2년 이내, KBS) : 2점
	<ul>
		<li>3,&nbsp;4급 1점/ 1, 2급&nbsp;2점</li>
	</ul>
	</li>
	<li>공인 영어성적(접수마감일 기준 2년 이내 성적- <strong><span style="color: rgb(0, 0, 205);">토익/토플 경우 국내/국외 정기시험만 가능, 특별/수시시험 불가</span></strong>)
	<ul>
		<li><strong><span style="color: rgb(0, 0, 255);">텝스성적기준은</span><span style="color: rgb(128, 0, 128);"> '21년 점수환산표' </span><span style="color: rgb(0, 0, 255);">적용에 따라 변경 ('22년 1회차('22년 4월입영) 부터 적용)</span></strong>
		<ul>
			<li>영어어학병은 가산점 부여 제외
			<table class="table_col" style="width: 629px; height: 108px;">
				<caption>영어어학병 가선점 부여 제외에 대한 표이며 구분/배점, 1점, 2점에 대한내용을 제공</caption>
				<thead>
					<tr>
						<th scope="row">구분 / 배점</th>
						<th scope="col">1점</th>
						<th scope="col">2점</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<th scope="row">TOEIC</th>
						<td style="text-align: center;">520 ~ 729</td>
						<td style="text-align: center;">730 이상</td>
					</tr>
					<tr>
						<th scope="row">TOEFL</th>
						<td style="text-align: center;">59 ~ 81</td>
						<td style="text-align: center;">82 이상</td>
					</tr>
					<tr>
						<th scope="row"><strong><span style="color: rgb(0, 0, 255);">New&nbsp;TEPS</span></strong></th>
						<td style="text-align: center;"><strong><span style="color: rgb(0, 0, 255);">201 ~276</span></strong></td>
						<td style="text-align: center;"><strong><span style="color: rgb(0, 0, 255);">277&nbsp;이상</span></strong>&nbsp;&nbsp;</td>
					</tr>
				</tbody>
			</table>
			</li>
		</ul>
		</li>
	</ul>
	</li>
</ul>
</div>"""