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
	<li>한국사능력검정(접수마감일 기준 최근 4년 이내, 국사편찬위원회) : 2점  <strong><span style="color: rgb(255, 0, 0);">* '25년 6회차 접수부터 폐지</span></strong>
	<ul>
		<li>3, 4급 1점/ 1, 2급 2점</li>
	</ul>
	</li>
	<li>한국어능력검정(접수마감일 기준&nbsp;최근 2년 이내, KBS) : 2점  <strong><span style="color: rgb(255, 0, 0);">* '25년 6회차 접수부터 폐지</span></strong>
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
html11="""<div class="layout_h4">
<h7>전문기술병(화생방, 의무, 기계, 공병, 통신전자전기, 차량정비, 차량운전, 전자계산)</h7>
<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="4" scope="col">서류전형(1차)</th>
			<th rowspan="2" scope="col">면접<br>
			(2차)</th>
			<th rowspan="2" scope="col">계</th>
		</tr>
		<tr>
			<th scope="col">자격/면허</th>
			<th scope="col">전공</th>
			<th scope="col">출결</th>
			<th scope="col">가산점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>50</td>
			<td>40</td>
			<td>10</td>
			<td>15</td>
			<td>25</td>
			<td>140</td>
		</tr>
	</tbody>
</table>
</div>"""
html12="""<div class="layout_h4">
<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="row">구분</th>
			<th colspan="3" scope="col">국가기술자격증</th>
			<th colspan="3" scope="col">일학습병행자격증</th>
			<th colspan="2" scope="col">일반자격증</th>
			<th colspan="3" scope="col"><span style="color: rgb(0, 0, 205);">운전면허증<br>
			(수송계열에 한함)</span></th>
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
			<th scope="col">대형/특수</th>
			<th scope="col">1종보통</th>
			<th scope="col">&nbsp; 2종보통(수동)&nbsp;</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">50</td>
			<td style="text-align: center;">45</td>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">50</td>
			<td style="text-align: center;">45</td>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">30</td>
			<td style="text-align: center;">26</td>
			<td style="text-align: center;">50</td>
			<td style="text-align: center;">45</td>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">20</td>
		</tr>
	</tbody>
</table>

</div>"""
html13="""<div class="layout_h4">
<table class="table_col">
	<thead>
		<tr>
			<th colspan="2" rowspan="3" scope="row">구분</th>
			<th colspan="8" scope="col">전공</th>
			<th rowspan="3" scope="col">비전공/<br>
			고퇴이하</th>
		</tr>
		<tr>
			<th colspan="2" scope="col">4년</th>
			<th colspan="2" scope="col">3년</th>
			<th colspan="2" scope="col">2년</th>
			<th colspan="2" scope="col">1년</th>
		</tr>
		<tr>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">대학교</th>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">38</td>
			<td style="text-align: center;">36</td>
			<td style="text-align: center;">34</td>
			<td style="text-align: center;">32</td>
			<td style="text-align: center;">30</td>
			<td style="text-align: center;">28</td>
			<td style="text-align: center;">26</td>
			<td rowspan="5" style="text-align: center;">20</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">전문대</th>
			<th scope="row">3년제</th>
			<td></td>
			<td></td>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">38</td>
			<td style="text-align: center;">36</td>
			<td style="text-align: center;">34</td>
			<td style="text-align: center;">32</td>
			<td style="text-align: center;">28</td>
		</tr>
		<tr>
			<th scope="row">2년제</th>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td style="text-align: center;">36</td>
			<td style="text-align: center;">34</td>
			<td style="text-align: center;">32</td>
			<td style="text-align: center;">28</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">고졸</th>
			<td colspan="8" style="text-align: center;">전공 34점, 비전공 20점</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">직업전문학교/<br>
			인력개발원</th>
			<td colspan="8">2년 수료 : 32점 / 1년 수료 ~ 2년 : 30점 / 6개월 ~ 1년 : 26점</td>
		</tr>
	</tbody>
</table>

<div><span style="font-size: 14px;">* 고교, 대학 등에서 관련학과를 모두 전공한 경우 배점을 비교하여 높은 점수 부여<br>
* <strong><span style="color: rgb(0, 0, 205);">차량운전 직종은 전공배점 적용 안함 (지원자 전원 20점 부여)</span></strong><br>
*&nbsp;한국폴리텍대학 :&nbsp;고용노동부 산하 / 인력개발원 : 대한상공회의소 산하</span>

<table class="table_col">
	<caption>학점은행제에 대한 표이며 학력인정기준학점, 배점(학사, 전문학사3년, 전문학사2년), 비고(대학학년)에 대한내용을 제공</caption>
	<tbody>
		<tr>
			<td rowspan="6" style="text-align: center;">학점은행제<br>
			*19년 1월 이후<br>
			접수자 부터 적용</td>
			<td colspan="1" rowspan="2" style="text-align: center;">학력인정<br>
			기준학점</td>
			<td colspan="3" rowspan="1" style="text-align: center;">배점</td>
			<td colspan="1" rowspan="2" style="text-align: center;">비고<br>
			(대학학년)</td>
		</tr>
		<tr>
			<td style="text-align: center;">학사</td>
			<td style="text-align: center;">전문학사<br>
			(3년)</td>
			<td style="text-align: center;">전문학사<br>
			(2년)</td>
		</tr>
		<tr>
			<td style="text-align: center;">40학점 이상</td>
			<td style="text-align: center;">28</td>
			<td style="text-align: center;">32</td>
			<td style="text-align: center;">32</td>
			<td style="text-align: center;">1학년</td>
		</tr>
		<tr>
			<td style="text-align: center;">80학점 이상</td>
			<td style="text-align: center;">32</td>
			<td style="text-align: center;">36</td>
			<td style="text-align: center;">36</td>
			<td style="text-align: center;">2학년</td>
		</tr>
		<tr>
			<td style="text-align: center;">120학점 이상</td>
			<td style="text-align: center;">36</td>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;"></td>
			<td style="text-align: center;">3학년</td>
		</tr>
		<tr>
			<td style="text-align: center;">140학점 이상</td>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;"></td>
			<td style="text-align: center;"></td>
			<td style="text-align: center;">4학년</td>
		</tr>
	</tbody>
</table>
<br>
</div>"""
html14="""<div class="layout_h4">
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
			<td>10</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
			<td>6</td>
			<td>고교3년간 누계적용</td>
		</tr>
	</tbody>
</table>
</div>"""
html15="""<div class="layout_h5">
<h6>&nbsp;일반기술병(일반계열)</h6>
<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="3" scope="col">서류전형</th>
			<th rowspan="2" scope="col">면접</th>
			<th rowspan="2" scope="col">계</th>
		</tr>
		<tr>
			<th scope="col">자격/면허</th>
			<th scope="col">출결</th>
			<th scope="col">가산점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">70</td>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: center;">110</td>
			<td style="text-align: center;">215</td>
		</tr>
	</tbody>
</table>
</div>"""
html16="""<div class="layout_h5">
<h6>&nbsp;전문기술병(전산, 조리, 항공, 전자, 통신, 기관, 화학, 전기, 건축/토목 등)</h6>

<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="4" scope="col">서류전형</th>
			<th rowspan="2" scope="col">면접</th>
			<th rowspan="2" scope="col">계</th>
		</tr>
		<tr>
			<th scope="col">자격/면허</th>
			<th scope="col">전공</th>
			<th scope="col">출결</th>
			<th scope="col">가산점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">50</td>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: center;">100</td>
			<td style="text-align: center;">215</td>
		</tr>
	</tbody>
</table>
</div>"""
html17="""<div class="layout_h3">
<h6>관련분야 직업경력자(전문기술 계열)</h6>
<table class="table_col">
	<thead>
		<tr>
			<th scope="row">2년 이상</th>
			<th scope="col">1년~2년 미만</th>
			<th scope="col">6개월~1년 미만</th>
			<th scope="col">6개월 미만</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">5점</th>
			<td style="text-align: center;">4점</td>
			<td style="text-align: center;">3점</td>
			<td style="text-align: center;">2점</td>
		</tr>
	</tbody>
</table>
<h6>컴퓨터속기 또는 한글속기 경력(전산계열 지원자에 한함)</h6>
<table class="table_col">
	<thead>
		<tr>
			<th scope="row">3년 이상</th>
			<th scope="col">1년 이상</th>
			<th scope="col">6월 이상</th>
			<th scope="col">속기 20편 이상</th>
			<th scope="col">속기 20편 미만</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">5점</th>
			<td style="text-align: center;"><strong>4점</strong></td>
			<td style="text-align: center;"><strong>3점</strong></td>
			<td style="text-align: center;"><strong>2점</strong></td>
			<td style="text-align: center;"><strong>1점</strong></td>
		</tr>
	</tbody>
</table>
<h6>독립유공자 (손)자녀, 국가 유공자&nbsp;자녀&nbsp;가산점 : 4점</h6>
<h6>질병치유 자원병역이행자 가산점 : 4점</h6>
<h6>국외이주자 중 현역복무지원자 가산점 : 4점</h6>
<h6>다자녀(3명 이상) 가정자녀&nbsp;가산점 : 4점 / 다자녀(2명) 가정자녀&nbsp;가산점 : 2점 (2021년 9월 입영자부터)</h6>
<h6>국민기초생활보장법 제7조제1항제1호에 따른 생계급여 수급권자 : 4점</h6>
<h6>수영관련 자격증(전 계열) : 2.5~5점<br>
잠수기능사&nbsp;5점 /&nbsp;수상안전 강사 5점 /&nbsp;인명구조 2.5점 /&nbsp;잠수자격 2.5점</h6>
<h6>건설기계(중장비) 운전 자격증(수송 계열) : 2.5점<br>
</div>"""
html18="""<div class="layout_h4">
<h6>&nbsp;일반기술병(일반, 수색)</h6>

<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="3" scope="col">1차</th>
			<th colspan="2" scope="col">2차</th>
			<th rowspan="2" scope="col">계<br>
			(1차+2차)</th>
		</tr>
		<tr>
			<th scope="col">자격/면허</th>
			<th scope="col">출결</th>
			<th scope="col">가산점</th>
			<th scope="col">면접</th>
			<th scope="col">체력검사</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">70</td>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: center;">80</td>
			<td style="text-align: center;">70</td>
			<td style="text-align: center;">255</td>
		</tr>
	</tbody>
</table>
</div>"""
html19="""<div class="layout_h4">
<h6>&nbsp;전문기술병(화학, 공병, 무기정비, 수송)</h6>
<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="4" scope="col">1차</th>
			<th colspan="2" scope="col">2차</th>
			<th rowspan="2" scope="col">계<br>
			(1차+2차)</th>
		</tr>
		<tr>
			<th scope="col">자격/면허</th>
			<th scope="col">전공</th>
			<th scope="col">출결</th>
			<th scope="col">가산점</th>
			<th scope="col">면접</th>
			<th scope="col">체력검사</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">50</td>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">10</td>
			<td>15</td>
			<td>70</td>
			<td>70</td>
			<td>255</td>
		</tr>
	</tbody>
</table>
</div>
"""
html20="""<div class="layout_h3">
<h3>체력검사&nbsp;: 배점 70점</h3>
<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="col">평가요소</th>
			<th colspan="2" scope="col">팔굽혀펴기</th>
			<th colspan="2" scope="col">윗몸일으키기</th>
		</tr>
		<tr>
			<th scope="col">횟수(1분)</th>
			<th scope="col">점수</th>
			<th scope="col">횟수(1분)</th>
			<th scope="col">점수</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="20" scope="row">등급/배점</th>
			<td>52회이상</td>
			<td>35</td>
			<td>58회이상</td>
			<td>35</td>
		</tr>
		<tr>
			<td>50~51</td>
			<td>34</td>
			<td>56~57</td>
			<td>34</td>
		</tr>
		<tr>
			<td>48~49</td>
			<td>33</td>
			<td>54~55</td>
			<td>33</td>
		</tr>
		<tr>
			<td>46~47</td>
			<td>32</td>
			<td>52~53</td>
			<td>32</td>
		</tr>
		<tr>
			<td>44~45</td>
			<td>31</td>
			<td>50~51</td>
			<td>31</td>
		</tr>
		<tr>
			<td>42~43</td>
			<td>30</td>
			<td>48~49</td>
			<td>30</td>
		</tr>
		<tr>
			<td>40~41</td>
			<td>29</td>
			<td>46~47</td>
			<td>29</td>
		</tr>
		<tr>
			<td>38~39</td>
			<td>28</td>
			<td>44~45</td>
			<td>28</td>
		</tr>
		<tr>
			<td>36~37</td>
			<td>27</td>
			<td>42~43</td>
			<td>27</td>
		</tr>
		<tr>
			<td>34~35</td>
			<td>26</td>
			<td>40~41</td>
			<td>26</td>
		</tr>
		<tr>
			<td>32~33</td>
			<td>25</td>
			<td>38~39</td>
			<td>25</td>
		</tr>
		<tr>
			<td>30~31</td>
			<td>24</td>
			<td>36~37</td>
			<td>24</td>
		</tr>
		<tr>
			<td>28~29</td>
			<td>23</td>
			<td>34~35</td>
			<td>23</td>
		</tr>
		<tr>
			<td>26~27</td>
			<td>22</td>
			<td>32~33</td>
			<td>22</td>
		</tr>
		<tr>
			<td>24~25</td>
			<td>21</td>
			<td>30~31</td>
			<td>21</td>
		</tr>
		<tr>
			<td>22~23</td>
			<td>20</td>
			<td>28~29</td>
			<td>20</td>
		</tr>
		<tr>
			<td>20~21</td>
			<td>19</td>
			<td>26~27</td>
			<td>19</td>
		</tr>
		<tr>
			<td>18~19</td>
			<td>18</td>
			<td>24~25</td>
			<td>18</td>
		</tr>
		<tr>
			<td>16~17</td>
			<td>17</td>
			<td>22~23</td>
			<td>17</td>
		</tr>
		<tr>
			<td>15회이하</td>
			<td>16</td>
			<td>21회이하</td>
			<td>16</td>
		</tr>
		<tr>
			<th scope="row">비고</th>
			<td colspan="4">* 전자측정 장비에 의하여 체력검사 실시(팔굽혀펴기 1분, 윗몸일으키기 1분)</td>
		</tr>
	</tbody>
</table>
</div>"""
html21="""<div class="layout_h3">
&nbsp;<span style="font-size: 14px;"><strong><span style="color: rgb(0, 0, 255);">&lt;공통가산점&gt; - 전계열</span></strong><br>
&nbsp;&nbsp; - 질병치유 자진입대 : 4점<br>
&nbsp;&nbsp; - 독립유공자 (손)자녀, 국가유공자 자녀 &nbsp;: 4점<br>
&nbsp;&nbsp; - 국외이주자 중 현역복무지원자 가산점 : 4점<br>
&nbsp;&nbsp; - 다자녀(3명 이상) 가정자녀&nbsp;가산점 : 4점 / 다자녀(2명) 가정자녀&nbsp;가산점 : 2점 <br>
&nbsp;&nbsp; -&nbsp;국민기초생활보장법 제7조제1항제1호에 따른 생계급여 수급권자 : 4점<br>
&nbsp;<strong><span style="color: rgb(0, 0, 255);"><span style="font-size: 14px;">&lt;기타 가산점&gt; - 수색 계열 제외</span></span></strong><br>
<span style="font-size: 14px;">&nbsp;&nbsp; - 무도 유단자 : 3단 이상 5점/ 1~2단 2점</span><br>
<span style="font-size: 14px;">&nbsp;&nbsp; -&nbsp;수상인명구조 자격증 소지자 : 2점<br>
&nbsp;&nbsp; - 공인회계사 자격증 소지자 : 삭제(2025년)</span>

<div>&lt;기타 가산점&gt; - 수색계열<br>
&nbsp;&nbsp; - 스키강사 자격증 소지자 : 10점<br>
&nbsp;&nbsp; - 스킨스쿠버 자격증 소지자 : 10점<br>
&nbsp;&nbsp; - 수영강사 자격증 소지자 : 10점<br>
&nbsp;&nbsp; - 무도유단자 : 3단이상 5점/ 1~2단 2점<br>
&nbsp;&nbsp; - 수상인명구조 자격증 소지자 : 5점</span><br>
&nbsp;병역진로설계 군 추천특기 지원자 가산점 : 1점</strong><br>
</div>"""
html31="""<div id="contents">
<div class="layout_h3">
<h3>지식재산관리병(311334)</h3>

<p>지식재산관리병은 군 관련 연구결과 특허출원 및 관리 임무를 수행합니다.</p>
</div>

<div class="layout_h3">
<h3>지원자격</h3>
<!--
<table class="table_row" style="width: 761px; height: 305px;">
-->

<table class="table_col">
	<caption>지원자격에 대한내용표이며 연령, 기본요건, 자격요건, 지원제한 대상에 대한내용을 제공</caption>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하 (2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>
			<ul class="list">
				<li>다음 중 어느하나에 해당되는 사람
				<ul>
					<li>신체등급&nbsp;1급부터 4급까지 현역병입영대상자로 병역처분된 사람</li>
					<li>병역판정검사를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 신체등급&nbsp;1급부터 4급까지 현역병입영대상자로 병역처분된 사람</li>
					<li>(단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은 최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>자격기준(아래 항목 중 한가지 이상 해당자)
				<ul>
					<li>변리사 자격증 소지자(최종시험 합격자 포함)</li>
					<li>특허 등록 5건 이상자(대리인 없는 단독 출원·등록, 단 법정대리인 예외)</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>&nbsp;○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라&nbsp;대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h3">
<h3>구비서류</h3>

<div class="layout_h4">
<h4>제출할 서류</h4>

<ul class="list">
	<li>최종 학력증명서(해당하는 사람)</li>
	<li>자격증 사본 1부(해당하는 사람)</li>
	<li>특허등록 원부&nbsp;1부(해당하는 사람)</li>
	<li>경력(재직)증명서 1부(해당하는 사람)
	<ul>
		<li>구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함.</li>
	</ul>
	</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3>지원서접수 및 전형일정</h3>

<p>접수 및 전형일정 알아보기(바로가기) : 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h3">
<h3>면접평가 장소</h3>

<ul class="list">
	<li>대전·충남지방병무청 모병면접실 (대전 중구 중앙로 16번길 5 대전충남지방병무청 내)
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h3">
<h3>선발 및 평가 배점<span style="font-size: 16px;">&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;</h3>

<ul class="list">
	<li>최종선발은 서류전형 점수와 면접평가 점수를 합하여 고득점순으로 결정됨
	<ul>
		<li>입영일자는 배점기준에 따른 고득자점순, 입영희망월 순으로 결정</li>
	</ul>
	</li>
</ul>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한내용표이며 총점, 경력, 전공학과, 자격증, 가산점, 면접에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">총점</th>
			<th scope="col">경력</th>
			<th scope="col">전공학과</th>
			<th scope="col">자격증</th>
			<th scope="col">면접</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td>25</td>
			<td>5</td>
			<td>20</td>
			<td>50</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3>경력(지식재산 관리 업무종사: 출원·등록·기술이전 등)</h3>

<table class="table_col">
	<caption>경력에 대한내용표이며 구분, 15개월이상, 12~14개월, 9~11개월, 6~8개월,&nbsp;3~5개월,&nbsp;2개월이하에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">15개월 이상</th>
			<th scope="col">12~14개월</th>
			<th scope="col">9~11개월</th>
			<th scope="col">6~8개월</th>
			<th scope="col">3~5개월</th>
			<th scope="col">2개월 이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>25</td>
			<td>23</td>
			<td>21</td>
			<td>19</td>
			<td>17</td>
			<td>15</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3>전공학과</h3>

<table class="table_col">
	<caption>전공학과에 대한내용표이며 구분, 특허 관련학과/ 이공계학과, 기타학과에 대한내용을 구분</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">특허 관련학과/이공계학과</th>
			<th scope="col">기타학과</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>5</td>
			<td>3</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp; * 특허 관련 학과<br>
&nbsp;&nbsp;&nbsp; 발명학과, 발명특허학과, 특허법률학과, 산업재산권학과, 특허법학과, 지식재산학<br>
&nbsp;&nbsp;&nbsp; 특허법무대학원, 지식재산대학원&nbsp;등<br>
&nbsp; * 이공계학과<br>
&nbsp;&nbsp;&nbsp; 생명과학, 화학, 기계공학, 재료공학, 컴퓨터공학, 전기/전자공학, 건설환경공학<br>
&nbsp;&nbsp;&nbsp; 화학생명공학, 건축토목, 산업공학 등&nbsp;관련 학과&nbsp;&nbsp;<br>
&nbsp;</p>

<div class="layout_h3">
<h3>자격증</h3>

<table class="table_col">
	<caption>자격증에 대한내용표이며 구분, 변리사, 기사, 산업기사, 무자격에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">변리사</th>
			<th scope="col">기사</th>
			<th scope="col">산업기사</th>
			<th scope="col">무자격</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>20</td>
			<td>18</td>
			<td>16</td>
			<td>14</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>한국산업인력공단 국가기술자격 중 아래 항목에 해당하는 자격증에 한하며, 등급이 높은 자격증 1개만 허용</li>
	<li>건축, 금속·재료, 기계장비설비·설치, 기계제작, 디자인, 안전관리, 자동차, 전기, 전자, 정보기술, 토목, 항공, 화공</li>
</ul>
</div>

<div class="layout_h3">
<h3>면접평가 배점표</h3>
</div>

<div class="layout_h3">
<table class="table_col">
	<caption>면접평가 배점표에 대한내용표이며 구분, 국가관, 적극성, 전공지식, 논리적, 지원동기에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">국가관</th>
			<th scope="col">적극성</th>
			<th scope="col">전공지식</th>
			<th scope="col">논리력</th>
			<th scope="col">지원동기</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>10</td>
			<td>10</td>
			<td>20</td>
			<td>5</td>
			<td>5</td>
		</tr>
	</tbody>
</table>
</div>
※ 면접점수 합계 50점 중 30 미만&nbsp;획득 시&nbsp;선발 제외&nbsp;처리
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html32="""<div id="contents">	                        
<div class="layout_h3">
<h3>훈련소조교병 (111292)</h3>

<div class="layout_h4">
<h4>훈련시범/지도, 신병훈육</h4>
</div>
</div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격에 대한내용표이며 연령, 기본요건, 신체요건, 지원제한 대상, 면접평가시 우대에 대한내용을 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_auto">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶&nbsp;신체등급 1급부터 2급까지&nbsp;현역병입영대상자로 병역처분된&nbsp; 사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 신체등급 1급부터 2급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된 사람</span></td>
		</tr>
		<tr>
			<th scope="row">신체요건</th>
			<td>
			<ul class="list">
				<li>신장 : 170Cm 이상, 체중 : 56Kg이상, 시력 : 교정시력 0.8이상</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>&nbsp;○ 문신자이 있는 사람, 디스크관절이상자<br>
			&nbsp;○ 범죄경력 조회결과(경찰청)<br>
			&nbsp; - 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			&nbsp; - 수사또는 재판중에 있는 사람<br>
			&nbsp; - 처분미상으로 통보된 사람- 집행유예 이상의 형을 선고받은 자 등<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
		<tr>
			<th scope="row">면접평가시 우대</th>
			<td>&nbsp;스카이다이빙, 스킨스쿠버, 스키, 인명구조관련자격소지자, 심리상담자격증 소지자, 각종무술 유단자</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p class="list">병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h3">
<h3>구비서류</h3>

<div class="layout_h4">
<h4>제출할 서류</h4>

<p>아래 서류 중 본인에게 해당하는 서류 제출</p>

<ul class="list">
	<li>무도단증 사본 1부(해당자)</li>
	<li>자격증 사본 1부(해당자)</li>
	<li>고등학교생활기록부 1부(검정고시, 외국소재 고등학교 졸업자 제출불요, 지원자의 평균점수 부여)</li>
	<li>국가유공자 자녀(독립유공자 손자녀 포함) 증명서 1부(해당자)</li>
	<li>지원서 작성 시 파일 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함.&nbsp;&nbsp;</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3>지원서접수 및 전형일정</h3>

<p>접수 및 전형일정 알아보기(바로가기) : 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 &nbsp;계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h3">
<h3>면접평가 장소</h3>

<ul class="list">
	<li>육군훈련소 입소대대 연무회관(충남 논산 연무 소재)
	<ul>
		<li>체력측정을 위한 운동복, 운동화를 꼭 지참하시기 바랍니다.</li>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h3">
<h3>선발 및 평가 배점</h3>

<div class="layout_h4">
<h4>아래 항목을 합하여 고득점 순으로 선발됨.</h4>

<p>※ 입영일자는 배점기준에 따른 고득자점순, 입영희망월 순으로 결정<br>
&nbsp;&nbsp; - 동점 시 선발기준 : 1차(생년월일이 빠른 순) / 최종(면접·실기 점수가 높은 순, 생년월일이 빠른 순)</p>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한내용표이며 구분, 서류심사(1차)( 고졸출석률, 무도단증, 자격증, 가산점), 면접/실기(2차)(면접, 체력측정)에 대한 내용을 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="4" scope="col">서류심사(1차)</th>
			<th colspan="2" scope="col">면접/실기(2차)</th>
		</tr>
		<tr>
			<th scope="col">고교출석률</th>
			<th scope="col">무도단증</th>
			<th scope="col">자격증</th>
			<th scope="col">가산점</th>
			<th scope="col">면접</th>
			<th scope="col">체력측정</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>20</td>
			<td>10</td>
			<td>5</td>
			<td>5</td>
			<td>30</td>
			<td>30</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>고교출석률</h4>

<table class="table_col">
	<caption>고교출석률에 대한내용표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 배점을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>배 점</td>
			<td>20</td>
			<td>18</td>
			<td>14</td>
			<td>8</td>
		</tr>
		<tr>
			<td colspan="5">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
&nbsp;

<h4>무도단증</h4>

<table class="table_col">
	<caption>무도단증에 대한내용표이며 구분, 3단 이상, 1~2단, 무단자에 대한 배점을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">3단 이상</th>
			<th scope="col">1~2단</th>
			<th scope="col">무단자</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>배 점</td>
			<td>10</td>
			<td>8</td>
			<td>6</td>
		</tr>
	</tbody>
</table>

<h4>자격증(생활체육, 인명구조, 교사, 심리상담사)</h4>

<table class="table_col">
	<caption>자격증(생활체육, 인명구조, 교사, 심리상담사)에 대한내용표이며 구분, 보유, 미보유에 대한 배점을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">보유</th>
			<th scope="col">미보유</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>배 점</td>
			<td>5</td>
			<td>4</td>
		</tr>
	</tbody>
</table>

<h4>가산점</h4>

<table class="table_col">
	<caption>가산점에 대한내용표이며 구분, 국가유공자 자녀(독립유동자 손/자녀 포함)에 대한 배점을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">국가유공자 자녀(독립유공자 손/자녀 포함)</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>배 점</td>
			<td>5</td>
		</tr>
	</tbody>
</table>

<h4>2차평가(면접/실기 평가 기준 및 배점표)</h4>

<div class="layout_h5">
<h5>체력평가</h5>

<div class="table_scroll">
<table class="table_col">
	<caption>2차평가에한 체력평가내용표이며 종목/점수, 윗몸일으키기(2분), 팔굽혀펴기(2분), 1.5km 달리기에 대한 내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">종목/점수</th>
			<td style="text-align: center;">15점</td>
			<td style="text-align: center;">13점</td>
			<td style="text-align: center;">11점</td>
			<td style="text-align: center;">9점</td>
			<td style="text-align: center;">7점</td>
			<td style="text-align: center;">5점</td>
			<td style="text-align: center;">0점</td>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">윗몸일으키키<br>
			(2분)</th>
			<td>82회 이상</td>
			<td>74∼81회</td>
			<td>66∼73회</td>
			<td>58∼65회</td>
			<td>50∼57회</td>
			<td>41∼49회</td>
			<td>40회 이하</td>
		</tr>
		<tr>
			<th scope="row">팔굽혀펴기<br>
			(2분)</th>
			<td>72회 이상</td>
			<td>64∼71회</td>
			<td>56∼63회</td>
			<td>48∼55회</td>
			<td>40∼47회</td>
			<td>31∼39회</td>
			<td>30회 이하</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong><span style="color: rgb(0, 0, 255);">* 1.5km 달리기 평가항목 제외('23년 1월 모집부터)</span></strong><br>
* 체력평가를 위해 운동복, 운동화 등 지참<br>
* 감염병 확산, 기상악화 등 상황에 따라 일부 종목 생략될 수 있음</p>
</div>
</div>

<div class="layout_h4">
<h4>면접평가</h4>

<table class="table_col">
	<caption>면접평가에 대한내용표</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">국가관/안보관</th>
			<th scope="col">품성/성장환경</th>
			<th scope="col">인성</th>
			<th scope="col">발표력</th>
			<th scope="col">면접태도</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>배 점</td>
			<td>6</td>
			<td>6</td>
			<td>6</td>
			<td>6</td>
			<td>6</td>
		</tr>
	</tbody>
</table>

<p><strong><span style="color: rgb(0, 0, 205);">※ 2차평가&nbsp;총점 60점 중 60%(36점) 미만 취득 시 선발제외('23년 1월 모집부터)</span></strong><br>
<br>
최종선발자는 육군훈련소에 입영 육군훈련소 조교로 근무 함</p>
</div>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html33="""<div id="contents">                     
<div class="layout_h3">
<h3>유해발굴감식병 (411294)</h3>

<div class="layout_h4">
<h4>발굴된 유해 감식임무 수행</h4>
</div>
</div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격에 대한 내용표이며 연령, 기본요건, 자격요건, 지원제한대상에 대한내용을 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중&nbsp;해당되는 사람<br>
			&nbsp; ▶&nbsp;신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된 사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 신체등급 1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된 사람</span></td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>자격기준(아래 항목 중 어느 하나에 해당되는 사람)
				<ul>
					<li>의(약)학, 물리치료학,&nbsp;치기공학, 간호학, 임상병리학,방사선학, 생물자원과, 동물자원과, 생물학, 화학, 생명공학,&nbsp;관련전공계열 1년&nbsp;재학 이상인 사람</li>
					<li>해부학 및 인골감식 관련 실험실 근무 경력&nbsp;3월 이상의 경력을 보유한 사람</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h3">
<h3>구비서류</h3>

<div class="layout_h4">
<h4>제출할 서류</h4>

<ul class="list">
	<li>최종 학력증명서(재학, 졸업 등) 1부</li>
	<li>경력증명서 1부(해당자만 제출)</li>
	<li>지원서 작성시 파일 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3>지원서접수 및 전형일정</h3>

<p>접수 및 전형일정 알아보기(바로가기) : 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집&nbsp; 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h3">
<h3>면접평가 장소</h3>

<ul class="list">
	<li>국방부 유해발굴감식단(서울 동작구 국립현충원 내) → 지하철 4호선 동작역 하차
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h3">
<h3>선발 및 평가 배점</h3>

<ul class="list">
	<li>서류전형과 면접평가 점수를 합하여 고득점자 순으로 최종선발됨</li>
	<li>평가부대 면접계획에 따라 총점 80점 미만은 지원자가 미달이어도&nbsp;선발제외 처리</li>
	<li>동점 시 선발기준&nbsp;:&nbsp;면접점수가 높은 순,&nbsp;생년월일이 빠른 순</li>
	<li>입영일자는 배점기준에 따른 고득자점 순, 입영희망월 순으로 결정</li>
</ul>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한내용표이며 계, 서류(발굴경력, 전공학과), 면접(국가관/가치관, 면접태도, 사명감/지원동기, 직무능력, 체력에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">계</th>
			<th colspan="2" scope="col">서류</th>
			<th colspan="5" scope="col">면접</th>
		</tr>
		<tr>
			<th scope="col">발굴경력</th>
			<th scope="col">전공학과</th>
			<th scope="col">국가관/가치관</th>
			<th scope="col">면접태도</th>
			<th scope="col">사명감/지원동기</th>
			<th scope="col">직무능력</th>
			<th scope="col">체력</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td>10</td>
			<td>10</td>
			<td>20</td>
			<td>20</td>
			<td>20</td>
			<td>10</td>
			<td>10</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>근무경력</h4>

<table class="table_col">
	<caption>근무경력에 대한내용표이며 구분, 1년이상, 6~11월, 3~5월, 1~2월 기본에 대한 배점을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">1년이상</th>
			<th scope="col">6~11월</th>
			<th scope="col">3~5월</th>
			<th scope="col">1~2월</th>
			<th scope="col">기 본</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>10</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
			<td>6</td>
		</tr>
	</tbody>
</table>

<h4>전공학과</h4>

<table class="table_col">
	<caption>전공학과에 대한 내용표이며 구분, 4년제졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 고졸이하에 대한 내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">4년제<br>
			졸업이상</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>10</td>
			<td>9.5</td>
			<td>9</td>
			<td>8.5</td>
			<td>8</td>
			<td rowspan="3">5</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>8</td>
			<td>7.5</td>
			<td>7</td>
			<td>6.5</td>
			<td>6</td>
		</tr>
		<tr>
			<th scope="row">기타학과</th>
			<td colspan="5">5</td>
		</tr>
	</tbody>
</table>

<h6>1. 직접학과 : 의(약)학,&nbsp; 방사선학, 물리치료학, 치기공학, 간호학, 임상병리학 계열<br>
2. 간접학과 :&nbsp;문화재보존학, 생물학, 동물학, 화학, 생명공학 계열</h6>

<h4>체력</h4>

<table class="table_col">
	<caption>체력에 대한내용표이며 구분, 연령, 등급(배점)(특급(5점)부터 5급(2.5점)까지의 내용을 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th rowspan="2" scope="col">연령</th>
			<th colspan="6" scope="col">등 급(배 점)</th>
		</tr>
		<tr>
			<th scope="col">특급(5점)</th>
			<th scope="col">1급(4.5점)</th>
			<th scope="col">2급(4점)</th>
			<th scope="col">3급(3.5점)</th>
			<th scope="col">4급(3점)</th>
			<th scope="col">5급(2.5점)</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="2" scope="row">팔굽혀펴기 (2분)</th>
			<td>25이하</td>
			<td>72이상</td>
			<td>64-71</td>
			<td>56-63</td>
			<td>48-55</td>
			<td>40-47</td>
			<td>39이하</td>
		</tr>
		<tr>
			<td>26-28</td>
			<td>70이상</td>
			<td>62-69</td>
			<td>54-61</td>
			<td>46-53</td>
			<td>38-45</td>
			<td>37이하</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">윗몸일으키기 (2분)</th>
			<td>25이하</td>
			<td>82이상</td>
			<td>74-81</td>
			<td>66-73</td>
			<td>58-65</td>
			<td>50-57</td>
			<td>49이하</td>
		</tr>
		<tr>
			<td>26-28</td>
			<td>80이상</td>
			<td>72-79</td>
			<td>64-71</td>
			<td>56-63</td>
			<td>48-55</td>
			<td>47이하</td>
		</tr>
	</tbody>
</table>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html34="""<div id="contents">
<div class="layout_h3">
<h3>의장병 (111284)</h3>

<p>각종 의장 행사 지원</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격에 대한내용표이며 연령, 기본요건, 신체요건, 지원제한 대상, 면접 시 우대에 대한내용을 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶&nbsp;신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 신체등급 </span>1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<span style="font-size: 13px;">&nbsp;</span></td>
		</tr>
		<tr>
			<th scope="row">신체요건</th>
			<td>
			<ul class="list">
				<li>신장 180cm 이상, 체중 65∼90kg</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>
			<ul>
				<li>디스크관절이상,&nbsp;수지결손, 수지강직, 운동/청력/언어&nbsp;장애, 수전증, 문신이 있는 사람</li>
				<li>정신건강의학과 질환이 있는 사람</li>
				<li>범죄조회 결과 징역 또는 금고의 형의 실형(집행유예포함)을 선고 받은 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">면접평가 시 우대</th>
			<td>무도단증 소지자 우대</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 →&nbsp;군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다</p>
</div>

<div class="layout_h5">
<h5>의장병 (111284)이 되면 이런 점이 좋다</h5>

<ul class="list">
	<li>서울 시내권 복무(국방부&nbsp;근무지원단 의장대대&nbsp;내&nbsp;복무가능)
	<ul>
		<li>&nbsp;복무가능부대 : 육군의장대,&nbsp;전통의장대, 현충원의장대, 연합사의장대, 본부중대</li>
		<li>&nbsp;육군 의장병 최종선발 합격 후 자대배치는 복무가능부대(5개부대) 부대인원 충원율 고려 배치</li>
		<li>&nbsp;전통의장대는 전문성 고려(전공학과, 무예관련 자격증 등) 우선 배치 할 수도 있음&nbsp;</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>무도 관련 자격증 사본 1부(해당자)</li>
	<li>고교생활기록부 사본 1부
	<ul>
		<li>지원서 작성시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함.</li>
	</ul>
	</li>
</ul>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<p>접수 및 전형일정 알아보기(바로가기) : 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집&nbsp; 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>면접평가 장소</h4>

<ul class="list">
	<li>국방광장(서울 용산구 국방부 내) ⇒ 지하철4호선 삼각지역 1번 출구
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<p>아래 항목을 합하여 고득점자 순으로 선발<br>
&nbsp;-&nbsp;동점 시 선발기준 :&nbsp;면접·체력평가 점수가 높은 순, 생년월일이 빠른 순</p>

<p>※ 입영일자는 배점기준에 따른 고득자점순, 입영희망월 순으로 결정</p>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한내용의표이며 계, 무도단증, 고교출석률,&nbsp;면접평가, 체력평가에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">계</th>
			<th scope="col">무도단증</th>
			<th scope="col">고교출석률</th>
			<th scope="col">면접평가</th>
			<th scope="col">체력평가</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td>10</td>
			<td>10</td>
			<td>35</td>
			<td>&nbsp;45</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>무도단증</h4>

<table class="table_col">
	<caption>무도단증에 대한내용표이며 구분, 태권도,합기도,검도, 기타 무도단증, 무단자에 대한 내용을 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">구 분</th>
			<th colspan="3" scope="col">&nbsp;&nbsp;태권도,합기도,검도</th>
			<th colspan="3" scope="col">기타 무도단증</th>
			<th rowspan="2" scope="col">무단자</th>
		</tr>
		<tr>
			<th scope="col">3단이상</th>
			<th scope="col">2단</th>
			<th scope="col">1단</th>
			<th scope="col">3단이상</th>
			<th scope="col">2단</th>
			<th scope="col">1단</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>10</td>
			<td>8</td>
			<td>6</td>
			<td>8</td>
			<td>6</td>
			<td>5</td>
			<td>4</td>
		</tr>
	</tbody>
</table>

<h4>고교출석률</h4>

<table class="table_col">
	<caption>고교출석률에 대한 표이며 구분, 결석0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 배점정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리
			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>

<h4>면접평가</h4>

<table class="table_col">
	<caption>면접에 대한 내용의 표이며 구분, 지원동기/표현능력, 신체/자격조건, 군인정신, 태도/외적자세, 국가관, 심리검사에 대한 배점을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">지원동기/<br>
			표현능력</th>
			<th scope="col">신체/<br>
			자격조건</th>
			<th scope="col">군인정신</th>
			<th scope="col">태도/<br>
			외적자세</th>
			<th scope="col">국가관</th>
			<th scope="col">심리검사</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>7</td>
			<td>7</td>
			<td>7</td>
			<td>7</td>
			<td>7</td>
			<td>합/불</td>
		</tr>
	</tbody>
</table>

<p>&nbsp; * 면접 항목별 배점 : A등급(7점), B등급(6점), C등급(5점), D등급(4점), E등급(불합격)<br>
&nbsp; * 불합격 기준 : 1개 항목 이상 불합격 시<br>
&nbsp;</p>

<h4>체력검정</h4>

<table class="table_col">
	<caption>체력평가에 대한 내용의 표이며 계, 팔굽혀펴기(2분이내), 윗몸일으키기(2분이내), 쪼그려뛰기(2분이내)에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">15점</th>
			<th scope="col">13점</th>
			<th scope="col">11점</th>
			<th scope="col">9점</th>
			<th scope="col">7점</th>
			<th scope="col">선발제외 대상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">팔굽혀펴기<br>
			(2분이내)</th>
			<td>60회 이상</td>
			<td>55~59회</td>
			<td>50~54회</td>
			<td>45~49회</td>
			<td>40~44회</td>
			<td>39회 이하</td>
		</tr>
		<tr>
			<th scope="row">윗몸일으키기<br>
			(2분이내)</th>
			<td>60회 이상</td>
			<td>55~59회</td>
			<td>50~54회</td>
			<td>45~49회</td>
			<td>40~44회</td>
			<td>39회 이하</td>
		</tr>
		<tr>
			<th scope="row">쪼그려뛰기<br>
			(2분이내)</th>
			<td>40회 이상</td>
			<td>35~39회</td>
			<td>30~34회</td>
			<td>25~29회</td>
			<td>20~24회</td>
			<td>19회 이하</td>
		</tr>
	</tbody>
</table>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html35="""<div id="contents">	                            
<div class="layout_h3">
<h3>유해발굴기록병 (111275)</h3>

<div class="layout_h4">
<h4>유해발굴 임무 수행</h4>
</div>
</div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격에 대한 내용표이며 연령, 기본요건, 자격요건, 지원제한대상에 대한내용을 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중&nbsp;해당되는 사람<br>
			&nbsp; ▶&nbsp;신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			&nbsp; ▶&nbsp;병역판정검사 결과 정형외과 질환, 천식, 피부질환,&nbsp;알레르기성 질환이 없는 사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과&nbsp;</span>1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<span style="font-size: 13px;">&nbsp;</span></td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>자격기준(아래 항목 중 어느 하나에&nbsp;해당되는 사람)
				<ul>
					<li>고고학과, 고고미술사학과, 고고인류학과, 사학과(동양/서양 사학과 포함), 문화인류학과, 문화재보존학과, 역사문화학, 역사학,&nbsp;역사교육학, 물리치료약,&nbsp;조소학 관련전공계열 1년&nbsp;재학 이상인 사람</li>
					<li>문화재/유해 발굴 3월 이상의 경력을 보유한 사람</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄경력 조회결과(경찰청)<br>
			&nbsp;&nbsp; - 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			&nbsp;&nbsp; - 수사또는 재판중에 있는 사람<br>
			&nbsp;&nbsp; - 처분미상으로 통보된 사람<br>
			○ 천식, 정형외과, 피부과, 알레르기 질환이 있는 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h3">
<h3>구비서류</h3>

<div class="layout_h4">
<h4>제출할 서류</h4>

<ul class="list">
	<li>최종 학력증명서(재학, 졸업 등) 1부</li>
	<li>경력증명서 1부(해당자만 제출)
	<ul>
		<li>지원서 작성시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함.</li>
	</ul>
	</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3>지원서접수 및 전형일정</h3>

<p>접수 및 전형일정 알아보기(바로가기) : 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집&nbsp; 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h3">
<h3>면접평가 장소</h3>

<ul class="list">
	<li>국방부 유해발굴감식단(서울 동작구 국립현충원 내) → 지하철 4호선 동작역 하차
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h3">
<h3>선발 및 평가 배점</h3>

<ul class="list">
	<li>서류전형과 면접평가 점수를 합하여 고득점자 순으로 최종선발됨
	<ul>
		<li>평가부대 면접계획에 따라 총점 80점 미만은 지원자가 미달이어도&nbsp;선발제외 처리</li>
		<li>동점 시 선발기준 :&nbsp;면접점수가 높은 순, 생년월일이 빠른 순</li>
	</ul>
	</li>
	<li>입영일자는 배점기준에 따른 고득자점 순, 입영희망월 순으로 결정</li>
</ul>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한내용표이며 계, 서류(발굴경력, 전공학과), 면접(국가관/가치관, 면접태도, 사명감/지원동기, 직무능력, 체력에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">계</th>
			<th colspan="2" scope="col">서류</th>
			<th colspan="5" scope="col">면접</th>
		</tr>
		<tr>
			<th scope="col">발굴경력</th>
			<th scope="col">전공학과</th>
			<th scope="col">국가관/가치관</th>
			<th scope="col">면접태도</th>
			<th scope="col">사명감/지원동기</th>
			<th scope="col">직무능력</th>
			<th scope="col">체력</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td>10</td>
			<td>10</td>
			<td>20</td>
			<td>20</td>
			<td>20</td>
			<td>10</td>
			<td>10</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>발굴경력</h4>

<table class="table_col">
	<caption>발굴경력에 대한내용표이며 1년이상, 6~11월, 3~5월, 1~2월, 기본에 대한 배점을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">1년이상</th>
			<th scope="col">6~11월</th>
			<th scope="col">3~5월</th>
			<th scope="col">1~2월</th>
			<th scope="col">기본</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>10</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
			<td>6</td>
		</tr>
	</tbody>
</table>

<h4>전공학과</h4>

<table class="table_col">
	<caption>전공학과에 대한내용표이며 구분, 4년제 졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학 고절이하에 대한 내용을 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">4년제<br>
			졸업이상</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>10</td>
			<td>9.5</td>
			<td>9</td>
			<td>8.5</td>
			<td>8</td>
			<td rowspan="3">5</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>8</td>
			<td>7.5</td>
			<td>7</td>
			<td>6.5</td>
			<td>6</td>
		</tr>
		<tr>
			<th scope="row">기타학과</th>
			<th colspan="5" scope="row">5</th>
		</tr>
	</tbody>
</table>

<h6>1. 직접학과 : 문화재보존학, 문화재관리학, 고고학,&nbsp;인류학, 역사문화학, 역사학계열<br>
2. 간접학과 : 역사교육학, 물리치료학, 조소학 계열</h6>

<h4>체력</h4>

<table class="table_col">
	<caption>체력에 대한내용표이며 구분, 연령, 등급(배점)(특급(5점)부터 5급(2.5점)까지의 내용을 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th rowspan="2" scope="col">연령</th>
			<th colspan="6" scope="col">등 급(배 점)</th>
		</tr>
		<tr>
			<th scope="col">특급(5점)</th>
			<th scope="col">1급(4.5점)</th>
			<th scope="col">2급(4점)</th>
			<th scope="col">3급(3.5점)</th>
			<th scope="col">4급(3점)</th>
			<th scope="col">5급(2.5점)</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="2" scope="row">팔굽혀펴기 (2분)</th>
			<td>25이하</td>
			<td>72이상</td>
			<td>64-71</td>
			<td>56-63</td>
			<td>48-55</td>
			<td>40-47</td>
			<td>39이하</td>
		</tr>
		<tr>
			<td>26-28</td>
			<td>70이상</td>
			<td>62-69</td>
			<td>54-61</td>
			<td>46-53</td>
			<td>38-45</td>
			<td>37이하</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">윗몸일으키기 (2분)</th>
			<td>25이하</td>
			<td>82이상</td>
			<td>74-81</td>
			<td>66-73</td>
			<td>58-65</td>
			<td>50-57</td>
			<td>49이하</td>
		</tr>
		<tr>
			<td>26-28</td>
			<td>80이상</td>
			<td>72-79</td>
			<td>64-71</td>
			<td>56-63</td>
			<td>48-55</td>
			<td>47이하</td>
		</tr>
	</tbody>
</table>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html36="""<div id="contents">	                          
<div class="layout_h3">
<h3>특전병 (112100)</h3>

<p>전국 6개&nbsp;지역대에 배치되어&nbsp;특수작전 지원&nbsp;임무를 수행한다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 신체요건, 지원제한 대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶&nbsp;신체등급 1급부터 2급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과&nbsp;</span>1급부터 2급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<span style="font-size: 13px;">&nbsp;</span></td>
		</tr>
		<tr>
			<th scope="row">신체요건</th>
			<td>
			<ul class="list">
				<li>시력 : 교정시력 0.8 이상</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>
			<ul>
				<li>디스크관절이상, 청력/언어/운동/색각 장애, 폐쇄공포증</li>
				<li>범죄조회 결과 집행유예 이상의 형을 선고받은 자, 수사또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련 사진, 관련 자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<p>아래 서류 중 본인에게 해당하는 서류 제출</p>

<ul class="list">
	<li>무도단증 사본 1부.</li>
	<li>자격증 사본 각 1부.</li>
	<li>고교생활기록부 사본 1부.
	<ul>
		<li>지원서 작성 시 첨부하지 않은 구비서류는 접수 마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</li>
	</ul>
	</li>
</ul>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접평가 장소</h4>

<ul class="list">
	<li>특전사령부 영외운동장(경기도 이천시 마장면 억만리로 137)</li>
	<li>체력측정을 위한 운동복, 운동화를 꼭 지참하시기 바랍니다.</li>
</ul>

<p>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</p>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<ul class="list">
	<li>1차 서류전형으로 3배수인원 선발 후, 2차 면접평가(체력측정 포함)를 실시함</li>
	<li>최종선발은 서류전형 점수와 면접/실기(체력)평가 점수를 합하여 고득점 순으로 결정됨</li>
	<li>동점 시 선발기준 : 1차(생년월일이 빠른 순) / 최종(면접·체력평가 점수가 높은 순, 생년월일이 빠른 순)</li>
</ul>

<p>입영일자는 배점기준에 따른 고득점자 순, 입영희망월 순으로 결정</p>

<table class="table_col">
	<caption>선발 및 평가 배점 표의 구분, 서류심사(1차), 면접/체력(2차), 신체등급 등의 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="3" scope="colgroup">서류심사(1차)</th>
			<th colspan="2" scope="colgroup">면접/체력(2차)</th>
		</tr>
		<tr>
			<th scope="col">무도단증</th>
			<th scope="col">자격증</th>
			<th scope="col">고교출석률</th>
			<th scope="col">체력평가</th>
			<th scope="col">면접평가</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>25</td>
			<td>15</td>
			<td>10</td>
			<td>20</td>
			<td>30</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>무도단증</h4>

<table class="table_col">
	<caption>무도단증에 대한 표이며 태권도,유도,검도, 기타 무도단증, 무단자에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="5" scope="colgroup">태권도,유도,검도</th>
			<th colspan="5" scope="colgroup">기타 무도단증</th>
			<th rowspan="2" scope="colgroup">무단자</th>
		</tr>
		<tr>
			<th scope="col">5단 이상</th>
			<th scope="col">4단</th>
			<th scope="col">3단</th>
			<th scope="col">2단</th>
			<th scope="col">1단</th>
			<th scope="col">5단 이상</th>
			<th scope="col">4단</th>
			<th scope="col">3단</th>
			<th scope="col">2단</th>
			<th scope="col">1단</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>25</td>
			<td>23</td>
			<td>21</td>
			<td>19</td>
			<td>17</td>
			<td>23</td>
			<td>21</td>
			<td>19</td>
			<td>17</td>
			<td>15</td>
			<td>10</td>
		</tr>
	</tbody>
</table>

<p>* 해당 무도단증 중 최상위 단만 인정<br>
&nbsp;</p>
&nbsp;

<h4>자격증</h4>

<table class="table_col">
	<caption>자격증에 대한 표이며 구분, 기사이상, 산업기사, 기능사에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">기사 이상</th>
			<th scope="col">산업기사</th>
			<th scope="col">기능사</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>8</td>
			<td>6</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="4" style="text-align: left;">*&nbsp;여러 개일 경우 합산 인정(최대 15점)<br>
			&nbsp; - 자격증은 종류별 가산 적용, ex) 정보처리기사, 사무자동화산업기사 → 14점<br>
			&nbsp; -&nbsp;동일 분야 최상위 등급만 인정 ex) 정보처리기사,&nbsp;정보처리기능사 → 8점&nbsp;<br>
			* 국가기술자격(기술/기능)분야에 한함</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;&nbsp;&nbsp;</p>

<h4>고교출석률</h4>

<table class="table_col">
	<caption>고교출석률에 대한 표이며, 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>

<h4>면접/실기 평가</h4>

<div class="layout_h5">
<h5>체력측정(2022. 4월 모집부터 적용)</h5>
&nbsp;

<p><span style="color: rgb(0, 0, 255);"><span style="font-size: 16px;">&nbsp;▶ 특전사령부 자체 체력평가 → 국민체력인증센터 '국민체력 100' 인증 등급으로 변경</span></span></p>

<h6><span style="color: rgb(0, 0, 0);">변경내용</span></h6>

<table class="table_col">
	<thead>
		<tr>
			<td style="width: 82px; height: 25px;">구 분</td>
			<td style="width: 192px; height: 25px;">기 존(~에서)</td>
			<td style="width: 331px; height: 25px;">변 경(~으로)</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="width: 82px; height: 29px;">수 행</td>
			<td style="width: 192px; height: 29px;">특전사령부</td>
			<td style="width: 331px; height: 29px;">국민체력인증센터</td>
		</tr>
		<tr>
			<td style="width: 82px; height: 175px;">평가종목</td>
			<td style="width: 192px; height: 175px;">① 1.5km 달리기<br>
			② 팔굽혀펴기<br>
			③ 윗몸일으키기<br>
			&nbsp;<br>
			&nbsp;<br>
			&nbsp;</td>
			<td style="width: 331px; height: 175px;">① 근력 : 상대악력<br>
			② 근지구력 : 교차윗몸일으키기<br>
			③ 심폐지구력(택1)<br>
			- 왕복 오래달리기, 트레드밀/스텝검사<br>
			④ 유연성 : 앉아 윗몸 앞으로 굽히기<br>
			⑤ 민첩성(택1) : 왕복달리기, 반응시간<br>
			⑥ 순발력 : 제자리멀리뛰기</td>
		</tr>
	</tbody>
</table>

<div data-hjsonver="1.0" data-jsonlen="25172">&nbsp;
<h6><span style="color: rgb(0, 0, 0);">등급별 배점</span></h6>

<table class="table_col">
	<thead>
		<tr>
			<td style="width: 62px; height: 25px;">구 분</td>
			<td style="width: 101px; height: 25px;">1급</td>
			<td style="width: 101px; height: 25px;">2급</td>
			<td style="width: 101px; height: 25px;">3급</td>
			<td style="width: 101px; height: 25px;">참여(등급외)</td>
			<td style="width: 139px; height: 25px;">미참여</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="width: 62px; height: 29px;">배 점</td>
			<td style="width: 101px; height: 29px;">20</td>
			<td style="width: 101px; height: 29px;">15</td>
			<td style="width: 101px; height: 29px;">10</td>
			<td style="width: 101px; height: 29px;">5</td>
			<td style="width: 139px; height: 29px;">선발제외</td>
		</tr>
	</tbody>
</table>

<p>* 국민체력100' 등급 기준 등 보다 자세한 사항은 '국민체력100 공식 누리집(홈페이지)' 참조<br>
&nbsp;&nbsp;(누리집(홈페이지) 주소 : <a href="https://nfa.kspo.or.kr">https://nfa.kspo.or.kr</a>)</p>
</div>
</div>

<div class="layout_h5">
<h5>면접평가</h5>

<table class="table_col">
	<caption>면접평가에 대한 표이며 계, 면접항목(발표력/표현력, 국가관, 추진력, 예절/태도, 품성, 대인관계역량)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">계</th>
			<th colspan="6" scope="colgroup">면접 항목</th>
		</tr>
		<tr>
			<th scope="col">발표력/표현력</th>
			<th scope="col">국가관</th>
			<th scope="col">추진력</th>
			<th scope="col">예절/태도</th>
			<th scope="col">품성</th>
			<th scope="col">대인관계역량</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
		</tr>
	</tbody>
</table>
</div>
&nbsp; ※ A(30점),&nbsp;B(25점), C(20점), D(15점),&nbsp;E(선발제외 처리)&nbsp;</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html37="""<div id="contents">	                           
<div class="layout_h3">
<h3>탐지분석병 (152296)</h3>

<p>탐지분석병은 전자매체 등을 이용한 지질탐사 관련 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원한 사람<br>
			○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶&nbsp;신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과&nbsp;</span>신체등급 1급부터 4급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<span style="font-size: 13px;">&nbsp;</span><br>
			&nbsp;&nbsp; &nbsp;(단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은<br>
			&nbsp; &nbsp;&nbsp;최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>자격기준(아래 항목 중 한 가지 이상 해당자)
				<ul>
					<li>전자공학, 전기공학, 전기정보공학, 지질학, 재료공학, 음향공학, 전산학, 자원공학 등 관련학과 3년 수료 이상자</li>
					<li>토목(산업)기사, 지적(산업)기사, 측량 및 지형공간정보(산업)기사 등 자격 취득자</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>&nbsp;○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>최종 학력증명서(재학, 졸업 등) 1부.</li>
	<li>자격증 사본 1부(해당자)</li>
	<li>고교생활기록부 사본 1부</li>
	<li>지원서 작성 시 첨부하지 않은 구비서류는 접수 마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</li>
</ul>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접/실기평가 장소</h4>

<ul class="list">
	<li>서울지방병무청 내 군지원센터(서울 영등포구 신길동 서울지방병무청 내) ⇒ 보라매전철역과 대방역 사이, 서울공고 방향 도보로 약10여 분 정도 소요
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<p>최종선발은 서류전형 점수와 면접평가 점수를 합하여 고득점순으로 결정됨<br>
&nbsp;* 동점 시 선발기준 :&nbsp;면접점수가 높은 순, 생년월일이 빠른 순</p>

<table class="table_col">
	<caption>선발 및 평가 배점 표이며 총점, 전공학과, 자격ㆍ면허증, 고교출석률, 면접 등의 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">총점</th>
			<th scope="col">전공학과</th>
			<th scope="col">자격·면허증</th>
			<th scope="col">고교출석률</th>
			<th scope="col">면접</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td>30</td>
			<td>20</td>
			<td>10</td>
			<td>40</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공학과</h5>

<table class="table_col">
	<caption>전공학과에 대한 표이며 구분, 대학원재학이상, 4년제졸업, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 고졸이하에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">대학원재학이상</th>
			<th scope="col">4년제졸업</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>30</td>
			<td>29</td>
			<td>28</td>
			<td>27</td>
			<td>26</td>
			<td>25</td>
			<td rowspan="3">20</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>27</td>
			<td>26</td>
			<td>25</td>
			<td>24</td>
			<td>23</td>
			<td>22</td>
		</tr>
		<tr>
			<th scope="row">기타학과</th>
			<td colspan="6">20</td>
		</tr>
	</tbody>
</table>

<div class="layout_h6">
<h6>&nbsp;1. 직접학과 : 전자공학, 컴퓨터, 정보통신, 물리학과, 지질학 계열<br>
&nbsp;2. 전산학 계열, 신소재공학, 음향공학, 자원공학, 지역시스템 공학</h6>
</div>

<h5>자격/면허증</h5>

<table class="table_col">
	<caption>자격/면허증에 대한 표이며 구분, 관련자격증, 무자격자에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th colspan="2" rowspan="2" scope="col">구분</th>
			<th colspan="3" scope="col">관련자격증</th>
			<th rowspan="2" scope="col">무자격자</th>
		</tr>
		<tr>
			<th scope="col">기사이상</th>
			<th scope="col">산업기사</th>
			<th scope="col">기능사</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th colspan="2" scope="row">배점</th>
			<td>20</td>
			<td>18</td>
			<td>16</td>
			<td rowspan="3">14</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">자격</th>
			<th scope="row">국가<br>
			기술</th>
			<td>탐사기술사, 토목시공기술사<br>
			토목기사, 정보통신기사 등</td>
			<td>지적산업기사, 토목산업기사<br>
			정보통신산업기사 등</td>
			<td>토목제도기능사,<br>
			웹디자인기능사,<br>
			웹마스터전문가</td>
		</tr>
		<tr>
			<th scope="row">일학습<br>
			병행</th>
			<td>측량 지리정보개발_L5,<br>
			정보통신설계_L5,<br>
			소음진동관리_L5,<br>
			토목설계_L5, SW개발_L5,<br>
			토목시공관리_L5,<br>
			광산조사ㆍ탐사_L5</td>
			<td>토목ㆍ건축관리_L3<br>
			토목설계_L3, SW개발_L3,<br>
			광산조사ㆍ탐사_L3</td>
			<td>측량 지리정보개발_L2</td>
		</tr>
	</tbody>
</table>

<h5>고교출석률</h5>

<table class="table_col">
	<caption>고교출석률에 대한 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">점수</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>
&nbsp;

<h5>면접평가</h5>

<table class="table_col">
	<caption>면접평가에 대한 표이며 구분, 지원동기, 면접태도, 대인관계역량, 표현력, 직무능력에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">지원동기</th>
			<th scope="col">면접태도</th>
			<th scope="col">대인관계역량</th>
			<th scope="col">표현력</th>
			<th scope="col">직무능력</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>20</td>
		</tr>
	</tbody>
</table>
* 면접접수 합계 40점 중 15점 미만 또는 1개 항목 이상 0점 시&nbsp;선발 제외&nbsp;처리&nbsp;
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>
	                        <form name="manjokdoForm" id="manjokdoForm">
	                            <div class="page_info">
	                                <div class="customer">
	                                    <div class="title">병무민원상담</div>
	                                    <ul>
	                                        <li id="minwonTel" class="tel"><span class="skip skip_m skip_t">전화번호</span> 1588-9090</li>
	                                        <!--<li id="minwonSms" class="sms"><span class="skip skip_m skip_t">문자보내기</span> #1110-9090</li> -->
	                                    </ul>
	                                </div>
	                                <div class="research">
	                                    <ul>
	                                        <li class="txt">현재 페이지의 정보에 만족하십니까?</li>
	                                        <li class="radio">
	                                            <span>
	                                                <input id="manjokdo_cd1" name="manjokdo_cd" type="radio" value="5">
	                                                <label for="manjokdo_cd1">매우만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd2" name="manjokdo_cd" type="radio" value="4">
	                                                <label for="manjokdo_cd2">만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd3" name="manjokdo_cd" type="radio" value="3">
	                                                <label for="manjokdo_cd3">보통</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd4" name="manjokdo_cd" type="radio" value="2">
	                                                <label for="manjokdo_cd4">불만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd5" name="manjokdo_cd" type="radio" value="1">
	                                                <label for="manjokdo_cd5">매우불만족</label>
	                                            </span>
	                                        </li>
	                                        <li class="input">
	                                            <label for="gtuigyeon_cn" class="skip_label">의견 입력란</label>
	                                            <input id="gtuigyeon_cn" name="gtuigyeon_cn" value="" type="text" onfocus="gtuigyeonChk();" onblur="gtuigyeonChk();">
	                                            <span class="button middle gray3">
	                                                <input value="반영" type="button" onclick="manjokdoInsert()" class="btn_button">
	                                            </span>
	                                        </li>
	                                    </ul>
	                                </div>
	                                <div class="info">
	                                    <ul>
	                                        <li id="ddbuseo_nm"><strong>담당정보 : </strong>현역모집과</li>
	                                        <li id="ddjikwon_fnm"><strong>담당자명 : </strong>이병희(042-481-2748)</li>
	                                        <li id="cjdatabyeongyeong_dtm"><strong>자료기준 : </strong>2023-02-23</li>
	                                    </ul>
	                                </div>
	                            </div>
	                        </form>
	                        <!-- container -->
	                    </div>"""
html38="""<div id="sub">
<div class="layout_h3">
<h3>특임군사경찰 (321102)</h3>

<p>특임군사경찰은 군 범인 검거 및 주요인사, 시설경호경비 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 신체요건, 지원제한 대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 2급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 2급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th scope="row">신체요건</th>
			<td>
			<ul class="list">
				<li>신장 168cm 이상, 교정시력 0.8 이상</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>
			<ul>
				<li>디스크관절이상, 운동/ 색각/청력/언어 장애,&nbsp;내반슬(오다리),&nbsp;치질,&nbsp;민소매/짧은 반바지 착용시 외관상 보이는 곳에 문신이 있는 경우</li>
				<li>범죄조회 결과 징역 또는 금고의 형의 실형(집행유예포함)을 선고 받은 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>고교 생활기록부 사본 1부</li>
	<li>무도단증 및 각종 자격증 사본 각 1부(해당자만 제출)</li>
	<li>최종학력증명서 1부(해당자만 제출)
	<ul>
		<li>지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함(가급적 접수기간 중에 제출될 수 있도록 사전에 구비서류를 준비하여, 서류미제출로 선발제외 되는 일이 없도록 하기 바람)</li>
	</ul>
	</li>
</ul>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접평가 장소(사정에 따라 변경될 수 있음)</h4>

<ul class="list">
	<li>수방사 군사경찰단(서울 관악구 남현동 남태령고개) ⇒ 지하철4호선 남태령역 3번출구 20m거리 군사경찰단 중문 입장
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정, 평가장소 등이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<div class="layout_h5">
<h5>1차 서류전형 3배수인원 선발후 2차 면접평가를 실시함</h5>

<ul class="list">
	<li>실기평가내용 : 체력측정(1.5km달리기, 팔굽혀펴기, 윗몸일으키기), 운동복, 운동화 지참 * 감염병 확산, 기상 상황에 따라 일부 종목 평가가 생략될 수 있음</li>
	<li>최종선발은 서류전형 점수와 면접/실기(체력)평가 점수를 합하여 고득점순으로 결정됨</li>
	<li>동점 시 선발기준 :&nbsp;무도단증 점수가 높은 순,&nbsp;출석률 점수가 높은 순, 생년월일이 빠른 순</li>
	<li>입영일자는 배점기준에 따른 고득자점순, 입영희망월 순으로 결정</li>
</ul>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한 표이며 계, 1차 서류전형, 2차 면접/체력 등의 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">계</th>
			<th colspan="4" scope="colgroup">1차 서류전형</th>
			<th colspan="2" scope="colgroup">2차 면접/체력 등</th>
		</tr>
		<tr>
			<th scope="col">무도단증</th>
			<th scope="col">전공</th>
			<th scope="col">고교출석률</th>
			<th scope="col">가산점(관련 자격증)</th>
			<th scope="col">면접</th>
			<th scope="col">체력</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td>15</td>
			<td>10</td>
			<td>10</td>
			<td>5</td>
			<td>40</td>
			<td>20</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>무도단증</h5>

<table class="table_col">
	<caption>무도단증에 대한 표이며 단수, 무도 4단 이상, 무도 3단, 무도 2단, 무도 1단에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">단 수</th>
			<th scope="col">무도 4단 이상</th>
			<th scope="col">무도 3단</th>
			<th scope="col">무도 2단</th>
			<th scope="col">무도 1단</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>15</td>
			<td>13</td>
			<td>11</td>
			<td>9</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: justify;">* 무도단증 2개 이상 시 높은 단수를 제외한 총단수에 가산점 부여(총단수X0.2점)<br>
			&nbsp;&nbsp; 예) 태권도 3단, 검도 2단 보유자 → 기본배점 13점+가산점(2X0.2)=13.4</td>
		</tr>
		<tr>
			<td colspan="5">
			<div style="text-align: justify;">&lt;대한체육회 가맹단체&gt;(10개)<br>
			대한태권도협회, 대한유도협회, 대한검도회, 대한카라데연맹, 대한택견회, 대한우슈협회, 대한복싱협회,<br>
			대한민국합기도총협회, 대한킥복싱협회, 대한주짓수회<br>
			&nbsp;<br>
			&lt;중앙본부 포함 8개 이상 광역 지방자치단체에 지부를 등록하고 3년 이상 활동 중인 단체(법인) 요건을 충족한 단체&gt;(51개)<br>
			대한기도회, 대한합기도협회, 세계합기도협회, 대한합기도총연맹, 대한합기도연맹, 국제연맹합기도중앙협회,<br>
			대한종합무술격투기협회, 대한합기도유술협회, 대한특공무술협회, 한국해동검도연합회, 한국해동검도협회,<br>
			K3세계국무도총연맹, 대한민국무무관합기도협회, 한국무예진흥원, 재남무술원, 대한신무합기도협회,<br>
			Korea합기도중앙협회,&nbsp; 대한합기도연합회, 국제특공무술연합회, 국제당수도연맹, 대한해동검도협회,<br>
			세계경찰무도연맹, 대한특공무술연맹,&nbsp;세계합기도연맹, 한국경호무술협회, 한국특공무술협회,<br>
			세계용무도연맹, 대한국술합기도협회,&nbsp;한민족합기도무술협회, 대한민국합기도중앙협회, 대한용무도협회,<br>
			세계합기도무도연맹, 신대한기도회합기도무술협회,&nbsp;대한호국특공무술총연맹, 대한검도연합회,<br>
			대한무에타이협회, 대한민국합기도협회, 국술원, 대한특수경호무술협회,&nbsp;대한민국해동검도협회,<br>
			대한민국합기도회, 대한생활체육복싱협회, ITF태권도협회, 특전사특공무술, 한국정통합기도협회,<br>
			한국국예원합기도협회, 세계태권무도연맹, 대한합기도총협회, 대한프로태권도협회, 한국킥복싱협회, 세계해동검도연맹<br>
			&lt;무예 분야 국가무형문화재 보유 단체&gt;(1개)<br>
			택견보존회</div>
			</td>
		</tr>
	</tbody>
</table>

<h5>전공점수</h5>

<table class="table_col">
	<caption>전공점수에 대한 표이며 구분, 4년제 졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">4년제<br>
			졸업이상</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row" style="text-align: center;">배점</th>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">2</td>
		</tr>
		<tr>
			<td colspan="6">
			<div style="text-align: left;">* 관련 전공학과<br>
			&lt;경찰 관련 학과&gt;<br>
			경찰법학과(부), 경찰행정학과(부), 경찰법행정학과(부), 법률경찰경호학과(부), 무도경찰행정, 법행정경찰학부,<br>
			경찰경호, 경찰경호행정, 경호경찰학과(부), 경찰행정경호학과(부), 경찰학과(부), 경찰태권도행정, 법경찰학과,<br>
			경찰경호학부, 부사관경찰경호,&nbsp;국방경찰행정학부, 법무경찰무도, 경찰경호스포츠, 경찰무도, 경찰소방,<br>
			경찰소방행정, 국제무도경호학부(경찰경호무도전공), 무도경찰학, 무도경찰행정, 행정경찰학과(부),&nbsp;<br>
			특공경찰전공, 경찰부사관과 등<br>
			&lt;소방 관련 학과&gt;<br>
			소방학과(부), 소방행정학과(부), 소방안전과(부), 소방대학, 소방안전구급과, 소방구조구급과,<br>
			재난안전소방학과, 안전소방학과(부), 소방방제학과(부)&nbsp;등<br>
			<span style="color: rgb(0, 0, 255);">&lt;무도 관련 학과&gt; - '23년 2월 모집부터 적용<br>
			경호무도학, 무도체육학, 무도학 등<br>
			&lt;스포츠 관련 학과&gt; - '23년 2월 모집부터 적용<br>
			체육교육학, 체육학, 사회체육학, 생활스포츠학, 생활체육학, 태권도학, 유도학 등</span></div>
			</td>
		</tr>
	</tbody>
</table>

<h5>고교출석률</h5>

<table class="table_col">
	<caption>고교출석률에 대한 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">점 수</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>

<h5>가산점</h5>

<table class="table_col">
	<caption>가산점에 대한 표이며 구분,&nbsp;일반경비지도사(한국산업인력공단)<br>
	응급구조사(한국보건의료인국가시험원),&nbsp;소방안전교육사(한국산업인력공단)<br>
	소방안전관리자(소방안전원)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">일반경비지도사(한국산업인력공단)<br>
			응급구조사(한국보건의료인국가시험원)</th>
			<th scope="col">소방안전교육사(한국산업인력공단)<br>
			소방안전관리자(소방안전원)</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배 점</th>
			<td>5</td>
			<td>3</td>
		</tr>
		<tr>
			<td colspan="3">&nbsp;* 각 항목에 해당하는 자격증 1개만&nbsp;인정<br>
			&nbsp;* 배점 3점 자격증 2개 보유자는 5점 인정</td>
		</tr>
	</tbody>
</table>

<h5>2차평가(면접/실기 평가 기준 및 배점표)</h5>

<div class="layout_h6">
<h6>체력평가</h6>

<table class="table_col">
	<caption>체력평가에 대한 표이며 1.5km달리기, 팔굽혀펴기(2분), 윗몸일으키키(2분), 종목별 배점에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th colspan="7" scope="col">종목별 배점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="2" scope="row"><strong>1.5Km<br>
			달리기</strong></th>
			<th><strong>0점</strong></th>
			<th><strong>2점</strong></th>
			<th><strong>4점</strong></th>
			<th><strong>6점</strong></th>
			<th><strong>8점</strong></th>
			<th><strong>10점</strong></th>
		</tr>
		<tr>
			<td>7분9초 이상</td>
			<td>6분49초<br>
			~7분8초</td>
			<td>6분29초<br>
			~6분48초</td>
			<td>6분9초<br>
			~6분28초</td>
			<td>5분49초<br>
			~6분8초</td>
			<td>5분48초<br>
			이하</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row"><strong>팔굽혀펴기<br>
			(2분)</strong></th>
			<th style="text-align: center;"><strong>0점</strong></th>
			<th style="text-align: center;"><strong>1점</strong></th>
			<th style="text-align: center;"><strong>2점</strong></th>
			<th style="text-align: center;"><strong>3점</strong></th>
			<th style="text-align: center;"><strong>4점</strong></th>
			<th style="text-align: center;"><strong>5점</strong></th>
		</tr>
		<tr>
			<td>39회 이하</td>
			<td>40~47회</td>
			<td>48~55회</td>
			<td>56~63회</td>
			<td>64~71회</td>
			<td>72회 이상</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row"><strong>윗몸일으키기<br>
			(2분)</strong></th>
			<th style="text-align: center;"><strong>0점</strong></th>
			<th style="text-align: center;"><strong>1점</strong></th>
			<th style="text-align: center;"><strong>2점</strong></th>
			<th style="text-align: center;"><strong>3점</strong></th>
			<th style="text-align: center;"><strong>4점</strong></th>
			<th style="text-align: center;"><strong>5점</strong></th>
		</tr>
		<tr>
			<td>49회 이하</td>
			<td>50~57회</td>
			<td>58~65회</td>
			<td>66~73회</td>
			<td>74~81회</td>
			<td>82회 이상</td>
		</tr>
	</tbody>
</table>

<p>*&nbsp;평가&nbsp;전종목&nbsp;0점 시 불합격 처리<br>
* 기상악화 등 상황에 따라 일부종목 생략될 수 있음<br>
&nbsp;</p>
</div>

<div class="layout_h6">
<h6>면접평가</h6>

<table class="table_col">
	<caption>면접평가에 대한 표이며 계, 발표/표현력, 자세/면접태도, 대인관계역량/희생정신, 학교생활/지원동기에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">계</th>
			<th scope="col">발표/표현력</th>
			<th scope="col">자세/면접태도</th>
			<th scope="col">대인관계역량/희생정신</th>
			<th scope="col">학교생활/지원동기</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">40점</th>
			<td>10</td>
			<td>10</td>
			<td>10</td>
			<td>10</td>
		</tr>
	</tbody>
</table>
</div>
*&nbsp;면전 합계 40점 중 60%(24점) 미만 취득 시&nbsp;선발 제외 처리&nbsp;</div>
</div>

<h4><span style="font-size: 14px;">유의사항&nbsp;: 입영 후 육군훈련소 인성검사 부적격 등 신체 및 자격조건 변경자와 병과교육 중 해당 군사특기 임무수행 부적격자는 다른 군사특기로 변경되어 복무할 수 있습니다</span><span style="font-size: 12px;">.</span></h4>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>
	                        <form name="manjokdoForm" id="manjokdoForm">
	                            <div class="page_info">
	                                <div class="customer">
	                                    <div class="title">병무민원상담</div>
	                                    <ul>
	                                        <li id="minwonTel" class="tel"><span class="skip skip_m skip_t">전화번호</span> 1588-9090</li>
	                                        <!--<li id="minwonSms" class="sms"><span class="skip skip_m skip_t">문자보내기</span> #1110-9090</li> -->
	                                    </ul>
	                                </div>
	                                <div class="research">
	                                    <ul>
	                                        <li class="txt">현재 페이지의 정보에 만족하십니까?</li>
	                                        <li class="radio">
	                                            <span>
	                                                <input id="manjokdo_cd1" name="manjokdo_cd" type="radio" value="5">
	                                                <label for="manjokdo_cd1">매우만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd2" name="manjokdo_cd" type="radio" value="4">
	                                                <label for="manjokdo_cd2">만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd3" name="manjokdo_cd" type="radio" value="3">
	                                                <label for="manjokdo_cd3">보통</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd4" name="manjokdo_cd" type="radio" value="2">
	                                                <label for="manjokdo_cd4">불만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd5" name="manjokdo_cd" type="radio" value="1">
	                                                <label for="manjokdo_cd5">매우불만족</label>
	                                            </span>
	                                        </li>
	                                        <li class="input">
	                                            <label for="gtuigyeon_cn" class="skip_label">의견 입력란</label>
	                                            <input id="gtuigyeon_cn" name="gtuigyeon_cn" value="" type="text" onfocus="gtuigyeonChk();" onblur="gtuigyeonChk();">
	                                            <span class="button middle gray3">
	                                                <input value="반영" type="button" onclick="manjokdoInsert()" class="btn_button">
	                                            </span>
	                                        </li>
	                                    </ul>
	                                </div>
	                                <div class="info">
	                                    <ul>
	                                        <li id="ddbuseo_nm"><strong>담당정보 : </strong>현역모집과</li>
	                                        <li id="ddjikwon_fnm"><strong>담당자명 : </strong>이병희(042-481-2748)</li>
	                                        <li id="cjdatabyeongyeong_dtm"><strong>자료기준 : </strong>2023-04-10</li>
	                                    </ul>
	                                </div>
	                            </div>
	                        </form>
	                        <!-- container -->
	                    </div>"""
html39="""<div id="sub">                     
<div class="layout_h3">
<h3>MC군사경찰 (321103)</h3>

<p>MC군사경찰은 오토바이 군사경찰로 주요인사 호위 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 신체요건, 지원제한 대상에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 2급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 2급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th scope="row">신체요건</th>
			<td>
			<ul class="list">
				<li>신장 175cm 이상, 시력(나안) 0.8 이상</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">&nbsp;※ 자동차 운전면허가 없어도 지원 가능</th>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>- 수지결손, 수지강직, 운동/청력/언어/색각장애기 있는 경우<br>
			- 민소매/짧은 반바지 착용시 외관상 보이는 곳에 문신이 있는 경우<br>
			- 범죄조회 결과 징역 또는 금고의 형의 실형(집행유예포함)을 선고 받은 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람<br>
			-&nbsp;'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>고교 생활기록부 사본 1부(대학학력자를 포함하여 지원자 전원 제출)</li>
	<li>자동차운전면허증, 자동차정비자격증 사본 각 1부(해당자만 제출)</li>
	<li>지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함.</li>
</ul>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접평가 장소</h4>

<ul class="list">
	<li>수방사 군사경찰단(서울 관악구 남현동 남태령고개) ⇒ 지하철4호선 남태령역 3번출구 20m거리 군사경찰단 중문 입장
	<ul>
		<li>병무청과 육군 사정에 따라&nbsp; 전형장소 및 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<div class="layout_h5">
<h5>1차 서류전형 3배수 인원 선발 후 2차 면접평가를 실시함</h5>

<ul class="list">
	<li>실기평가내용 :&nbsp;체력측정(1.5km달리기, 팔굽혀펴기, 윗몸일으키기), 운동복, 운동화 지참</li>
	<li>최종선발은 서류전형 점수와 면접/실기(체력)평가 점수를 합하여 고득점순으로 결정됨</li>
	<li>동점 시 선발기준 :&nbsp;운전면허 점수가 높은 순, 가산점이 높은 순, 출석률 점수가 높은 순, 생년월일이 빠른 순</li>
	<li>입영일자는 배점기준에 따른 고득자점순, 입영희망월 순으로 결정</li>
</ul>

<table class="table_col">
	<caption>서류전형, 면접/체력 표이며 총점, 서류심사(1차), 면접/체력(2차), 면접에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="3" scope="col">총점</th>
			<th colspan="3" scope="colgroup">서류심사(1차)</th>
			<th colspan="4" scope="colgroup">면접/체력(2차)</th>
		</tr>
		<tr>
			<th rowspan="2" scope="col">자동차<br>
			운전면허</th>
			<th rowspan="2" scope="col">고교출석률</th>
			<th rowspan="2" scope="col">&nbsp;&nbsp;가산점</th>
			<th colspan="3" scope="col">체력</th>
			<th rowspan="2" scope="col">면접</th>
		</tr>
		<tr>
			<th scope="col">윗몸일으키기</th>
			<th scope="col">팔굽혀펴기</th>
			<th scope="col">1.5km 달리기</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">35</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5"></div>

<div class="layout_h5">
<h5>운전면허</h5>

<table class="table_col">
	<caption>운전면허에 대한 표이며 구분, 자동차운전면허 소지(종류구분없음), 없음에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">자동차운전면허 소지<br>
			(종류 구분 없음)</th>
			<th scope="col">없음</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">0</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>고교출석률</h5>

<table class="table_col">
	<caption>고교출석률에 대한 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">점 수</th>
			<td>20</td>
			<td>18</td>
			<td>15</td>
			<td>10</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>2차평가(면접/실기 평가 기준 및 배점표)</h5>

<div class="layout_h6">
<h6>체력평가(1)</h6>

<table class="table_col">
	<caption>체력평가에 대한 표이며 종목/점수, 0점, 6점, 7점, 8점, 9점, 10점에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">종목/점수</th>
			<th scope="col">0점</th>
			<th scope="col">6점</th>
			<th scope="col">7점</th>
			<th scope="col">8점</th>
			<th scope="col">9점</th>
			<th scope="col">10점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">윗몸일으키기<br>
			(2분)</th>
			<td>49회 이하</td>
			<td>50~59회</td>
			<td>60~69회</td>
			<td>70~79회</td>
			<td>80~89회</td>
			<td>90회 이상</td>
		</tr>
		<tr>
			<th scope="row">팔굽혀펴기<br>
			(2분)</th>
			<td>39회 이하</td>
			<td>40~49회</td>
			<td>50~59회</td>
			<td>60~69회</td>
			<td>70~79회</td>
			<td>80회 이상</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h6">
<h6>체력평가(2)</h6>

<table class="table_col">
	<caption>체력평가 표이며 1.5km달리기에 대한 점수의 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">종목/점수</th>
			<th scope="col">0점</th>
			<th scope="col">6점</th>
			<th scope="col">7점</th>
			<th scope="col">8점</th>
			<th scope="col">9점</th>
			<th scope="col">10점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">1.5Km<br>
			달리기</th>
			<td>7분9초이상</td>
			<td>6분39초<br>
			~7분8초</td>
			<td>6분9초<br>
			~6분38초</td>
			<td>5분31초<br>
			~6분8초</td>
			<td>4분39초<br>
			~5분30초</td>
			<td>4분38초이하</td>
		</tr>
	</tbody>
</table>
</div>
<br>
*&nbsp;평가&nbsp;전종목&nbsp;0점 시&nbsp;선발 제외&nbsp;처리<br>
* 기상악화 등 상황에 따라 일부종목 생략될 수 있음<br>
&nbsp;
<div class="layout_h6">
<h6>면접평가</h6>

<table class="table_col">
	<caption>면접평가에 대한 표이며 지원동기, 발표력/표현력, 면접태도, 학교생활/관련학과,&nbsp; 국가관/대인관계역량에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">계</th>
			<th scope="col">지원동기</th>
			<th scope="col">발표력/표현력</th>
			<th scope="col">면접태도</th>
			<th scope="col">학교생활/관련학과</th>
			<th scope="col">국가관/대인관계역량</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">35</th>
			<td>5</td>
			<td>5</td>
			<td>10</td>
			<td>5</td>
			<td>10</td>
		</tr>
	</tbody>
</table>
</div>
&nbsp;* 면접 합계 35점 중 60%(21점) 미만 취득 시 선발 제외 처리</div>
</div>

<h4><span style="font-size: 14px;">유의사항&nbsp;: 입영 후 육군훈련소 인성검사 부적격 등 신체 및 자격조건 변경자와 병과교육 중 해당 군사특기 임무수행 부적격자는 다른 군사특기로 변경되어 복무할 수 있습니다</span><span style="font-size: 12px;">.</span>&nbsp;</h4>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>
	                        <form name="manjokdoForm" id="manjokdoForm">
	                            <div class="page_info">
	                                <div class="customer">
	                                    <div class="title">병무민원상담</div>
	                                    <ul>
	                                        <li id="minwonTel" class="tel"><span class="skip skip_m skip_t">전화번호</span> 1588-9090</li>
	                                        <!--<li id="minwonSms" class="sms"><span class="skip skip_m skip_t">문자보내기</span> #1110-9090</li> -->
	                                    </ul>
	                                </div>
	                                <div class="research">
	                                    <ul>
	                                        <li class="txt">현재 페이지의 정보에 만족하십니까?</li>
	                                        <li class="radio">
	                                            <span>
	                                                <input id="manjokdo_cd1" name="manjokdo_cd" type="radio" value="5">
	                                                <label for="manjokdo_cd1">매우만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd2" name="manjokdo_cd" type="radio" value="4">
	                                                <label for="manjokdo_cd2">만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd3" name="manjokdo_cd" type="radio" value="3">
	                                                <label for="manjokdo_cd3">보통</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd4" name="manjokdo_cd" type="radio" value="2">
	                                                <label for="manjokdo_cd4">불만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd5" name="manjokdo_cd" type="radio" value="1">
	                                                <label for="manjokdo_cd5">매우불만족</label>
	                                            </span>
	                                        </li>
	                                        <li class="input">
	                                            <label for="gtuigyeon_cn" class="skip_label">의견 입력란</label>
	                                            <input id="gtuigyeon_cn" name="gtuigyeon_cn" value="" type="text" onfocus="gtuigyeonChk();" onblur="gtuigyeonChk();">
	                                            <span class="button middle gray3">
	                                                <input value="반영" type="button" onclick="manjokdoInsert()" class="btn_button">
	                                            </span>
	                                        </li>
	                                    </ul>
	                                </div>
	                                <div class="info">
	                                    <ul>
	                                        <li id="ddbuseo_nm"><strong>담당정보 : </strong>현역모집과</li>
	                                        <li id="ddjikwon_fnm"><strong>담당자명 : </strong>이병희(042-481-2748)</li>
	                                        <li id="cjdatabyeongyeong_dtm"><strong>자료기준 : </strong>2023-04-10</li>
	                                    </ul>
	                                </div>
	                            </div>
	                        </form>
	                        <!-- container -->
	                    </div>"""
html40="""<div id="sub">
<div class="layout_h3">
<h3>33경호병 (321273)</h3>

<p>33경호병은 주요인사 경호, 주요시설 경비업무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 신체요건, 지원제한 대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 2급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 2급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th scope="row">신체요건</th>
			<td>
			<ul class="list">
				<li>신장 175cm 이상~ 190cm 이하, 체중 90kg 이하, 시력(나안) 0.8 이상</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄조회 결과 징역 또는 금고의 형의 실형(집행유예포함)을 선고 받은 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>최종 학력증명서(재학, 졸업 등) 1부</li>
	<li>각종 자격증 사본 각 1부(해당자만 제출)</li>
	<li>무도단증 사본 1부(해당자만 제출)</li>
	<li>고교생활기록부 사본 1부
	<ul>
		<li>지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함.</li>
	</ul>
	</li>
</ul>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접/실기평가 장소(집결)</h4>

<ul class="list">
	<li>수방사 군사경찰단(서울 관악구 남현동 남태령고개) ⇒ 지하철4호선 남태령역 3번출구 20m거리 군사경찰단 중문 입장</li>
	<li>병무청과 육군 사정에 따라&nbsp; 전형장소 및 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<div class="layout_h5">
<h5>1차 서류전형 4배수인원 선발후 2차 면접평가를 실시함</h5>

<ul class="list">
	<li>실기평가내용 : 해당 무도 기본동작, 체력측정(1.5km달리기, 팔굽혀펴기, 윗몸일으키기), 무도복(운동복), 운동화 지참</li>
	<li>최종선발은 서류전형 점수와 면접/실기평가 점수를 합하여 고득점순으로 결정됨</li>
	<li>동점 시 선발기준 : 무도단증 점수가 높은 순, 생년월일이 높은 순</li>
	<li>입영일자는 배점기준에 따른 고득점자부터 입영희망월을 반영하여 결정</li>
</ul>

<table class="table_col">
	<caption>서류심사, 면접/실기에 대한 표이며 계, 서류심사(1차), 면접/ 실기(2차) 등의 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">계</th>
			<th colspan="4" scope="colgroup">서류심사(1차)</th>
			<th colspan="3" scope="colgroup">면접/실기(2차)</th>
		</tr>
		<tr>
			<th scope="col">전공</th>
			<th scope="col">무도단증</th>
			<th scope="col">고교출석률</th>
			<th scope="col">가산점</th>
			<th scope="col">체력</th>
			<th scope="col">무도</th>
			<th scope="col">면접</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">150</th>
			<td>15</td>
			<td>20</td>
			<td>10</td>
			<td>5</td>
			<td>40</td>
			<td>20</td>
			<td>40</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<caption>전공에 대한 표이며 구분, 대학원 재학이상, 4년제 졸업, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 고졸이하에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">대학원<br>
			재학이상</th>
			<th scope="col">4년제 졸업</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>15</td>
			<td>14</td>
			<td>13</td>
			<td>12</td>
			<td>11</td>
			<td>10</td>
			<td rowspan="3">7</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>13</td>
			<td>12</td>
			<td>11</td>
			<td>10</td>
			<td>9</td>
			<td>8</td>
		</tr>
		<tr>
			<th scope="row">기타학과</th>
			<td colspan="6">7</td>
		</tr>
	</tbody>
</table>

<div class="layout_h6">
<h6>1. 직접학과 : 경호학계열, 경기지도학 계열, 무도 계열, 경찰 계열, 체육계열, 스포츠 계열<br>
2. 간접학과 : 스포츠(과학,복지,산업,레저복지), 특수체육계열, 동양무예 계열</h6>
</div>
</div>

<div class="layout_h5">
<h5>무도단증</h5>

<table class="table_col">
	<caption>무도단증에 대한 표이며 단수, 무도4단이상, 무도3단, 무도2단, 무도1단에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">단수</th>
			<th scope="col">무도4단이상</th>
			<th scope="col">무도3단</th>
			<th scope="col">무도2단</th>
			<th scope="col">무도1단</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>20</td>
			<td>16</td>
			<td>12</td>
			<td>10</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: justify;">&nbsp;* 무도단증 2개 이상 시 높은 단수를 제외한 총단수에 가산점 부여(총단수X0.2점)<br>
			&nbsp;&nbsp; 예) 태권도 3단, 검도 2단 보유자 → 기본배점 16점+가산점(2X0.2)=16.4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: justify;">
			<div data-hjsonver="1.0" data-jsonlen="7054"><span style="color: rgb(0, 0, 0);">&lt;대한체육회 가맹단체&gt;(10개)<br>
			대한태권도협회, 대한유도회, 대한검도회, 대한카라데연맹, 대한택견회, 대한우슈협회, 대한복싱협회,<br>
			대한민국합기도총협회, 대한킥복싱협회, 대한주짓수회</span><br>
			&nbsp;<br>
			<span style="color: rgb(0, 0, 0);">&lt;중앙본부 포함 8개 이상 광역 지방자치단체에 지부를 등록하고 3년 이상 활동 중인 단체(법인) 요건을 충족한 단체&gt;(51개)<br>
			대한기도회, 대한합기도협회, 세계합기도협회, 대한합기도총연맹, 대한합기도연맹, 국제연맹합기도중앙협회,<br>
			대한종합무술격투기협회, 대한합기도유술협회, 대한특공무술협회, 한국해동검도연합회, 한국해동검도협회,<br>
			K3세계국무도총연맹, 대한민국무무관합기도협회, 한국무예진흥원, 재남무술원, 대한신무합기도협회,<br>
			Korea합기도중앙협회, 대한합기도연합회, 국제특공무술연합회, 국제당수도연맹, 대한해동검도협회,<br>
			세계경찰무도연맹, 대한특공무술연맹, 세계합기도연맹, 한국경호무술협회, 한국특공무술협회,<br>
			세계용무도연맹,&nbsp; 대한국술합기도협회, 한민족합기도무술협회, 대한민국합기도중앙협회, 대한용무도협회,<br>
			세계합기도무도연맹, 신대한기도회합기도무술협회, 대한호국특공무술연맹, 대한검도연합회,<br>
			대한무에타이협회, 대한민국합기도협회, 국술원, 대한특수경호무술협회, 대한민국해동검도협회,<br>
			대한민국합기도회, 대한생활체육복싱협회, ITF태권도협회, 특전사특공무술, 한국정통합기도협회,<br>
			대한국예원합기도협회, 세계태권무도연맹, 대한합기도총협회, 대한프로태권도협회, 한국킥복싱연맹<br>
			세계해동검도연맹</span><br>
			&nbsp;<br>
			&lt;무예 분야 국가무형문화재 보유 단체&gt;(1개)<br>
			택견보존회</div>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5"></div>

<div class="layout_h5"></div>

<div class="layout_h5">
<h5>고교출석률</h5>

<table class="table_col">
	<caption>고교출석률에 대한 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">점 수</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>가산점</h5>

<table class="table_col">
	<caption>가산점에 대한 표이며 갯수, 4개, 3개, 2개, 1개, 자격 미소지자에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_10p">
		<col class="width_18p">
		<col class="width_18p">
		<col class="width_18p">
		<col class="width_18p">
		<col class="width_18p">
	</colgroup>
	<thead>
		<tr>
			<th scope="col">갯 수</th>
			<th scope="col">4개</th>
			<th scope="col">3개</th>
			<th scope="col">2개</th>
			<th scope="col">1개</th>
			<th scope="col">자격 미소지자</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="2" scope="row">배 점</th>
			<td>5</td>
			<td>4</td>
			<td>3</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td colspan="5">무도를 제외한 자격증 취득건수</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>2차평가(면접/실기 평가 기준 및 배점표)</h4>

<h6>체력평가</h6>

<table class="table_col">
	<caption>체력평가에 대한 표이며 종목별 배점에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th colspan="7" scope="col">종목별 배점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="2" scope="row"><strong>1.5Km<br>
			달리기</strong></th>
			<th><strong>0점</strong></th>
			<th><strong>4점</strong></th>
			<th><strong>8점</strong></th>
			<th><strong>12점</strong></th>
			<th><strong>16점</strong></th>
			<th><strong>20점</strong></th>
		</tr>
		<tr>
			<td>7분9초 이상</td>
			<td>6분49초<br>
			~7분8초</td>
			<td>6분29초<br>
			~6분48초</td>
			<td>6분9초<br>
			~6분28초</td>
			<td>5분49초<br>
			~6분8초</td>
			<td>5분48초<br>
			이하</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row"><strong>팔굽혀펴기<br>
			(2분)</strong></th>
			<th style="text-align: center;"><strong>0점</strong></th>
			<th style="text-align: center;"><strong>2점</strong></th>
			<th style="text-align: center;"><strong>4점</strong></th>
			<th style="text-align: center;"><strong>6점</strong></th>
			<th style="text-align: center;"><strong>8점</strong></th>
			<th style="text-align: center;"><strong>10점</strong></th>
		</tr>
		<tr>
			<td>39회 이하</td>
			<td>40~47회</td>
			<td>48~55회</td>
			<td>56~63회</td>
			<td>64~71회</td>
			<td>72회 이상</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row"><strong>윗몸일으키기<br>
			(2분)</strong></th>
			<th style="text-align: center;"><strong>0점</strong></th>
			<th style="text-align: center;"><strong>2점</strong></th>
			<th style="text-align: center;"><strong>4점</strong></th>
			<th style="text-align: center;"><strong>6점</strong></th>
			<th style="text-align: center;"><strong>8점</strong></th>
			<th style="text-align: center;"><strong>10점</strong></th>
		</tr>
		<tr>
			<td>49회 이하</td>
			<td>50~57회</td>
			<td>58~65회</td>
			<td>66~73회</td>
			<td>74~81회</td>
			<td>82회 이상</td>
		</tr>
	</tbody>
</table>

<div class="layout_h5">
<p>&nbsp;*&nbsp;평가&nbsp;전종목&nbsp;0점 시&nbsp;선발 제외 처리<br>
&nbsp;* 기상악화 등 상황에 따라 일부종목 생략될 수 있음</p>
</div>

<div class="layout_h5">
<h5>무도평가</h5>

<table class="table_col">
	<caption>무도평가에 대한 표이며 계, 품세(본), 특기술, 자유대련에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">계</th>
			<th scope="col">품세(본)</th>
			<th scope="col">특기술</th>
			<th scope="col">자유대련</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">20점</th>
			<td>5점</td>
			<td>10점</td>
			<td>5점</td>
		</tr>
	</tbody>
</table>

<p>* 실기평가 미실시자 0점 부여</p>
</div>

<div class="layout_h5">
<h5>면접평가</h5>

<table class="table_col">
	<caption>면접평가에 대한 표이며 계, 표현/의사소통, 자세/면접태도, 품성/국가관, 대인관계역량, 건강상태/체격에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">계</th>
			<th scope="col">표현/의사소통</th>
			<th scope="col">자세/면접태도</th>
			<th scope="col">품성/국가관</th>
			<th scope="col">대인관계역량</th>
			<th scope="col">건강상태/체격</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">40점</th>
			<td>10점</td>
			<td>5점</td>
			<td>10점</td>
			<td>5점</td>
			<td>10점</td>
		</tr>
	</tbody>
</table>
</div>
</div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 40점 중 60%(24점) 미만 취득 시 불합격
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>
	                        <form name="manjokdoForm" id="manjokdoForm">
	                            <div class="page_info">
	                                <div class="customer">
	                                    <div class="title">병무민원상담</div>
	                                    <ul>
	                                        <li id="minwonTel" class="tel"><span class="skip skip_m skip_t">전화번호</span> 1588-9090</li>
	                                        <!--<li id="minwonSms" class="sms"><span class="skip skip_m skip_t">문자보내기</span> #1110-9090</li> -->
	                                    </ul>
	                                </div>
	                                <div class="research">
	                                    <ul>
	                                        <li class="txt">현재 페이지의 정보에 만족하십니까?</li>
	                                        <li class="radio">
	                                            <span>
	                                                <input id="manjokdo_cd1" name="manjokdo_cd" type="radio" value="5">
	                                                <label for="manjokdo_cd1">매우만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd2" name="manjokdo_cd" type="radio" value="4">
	                                                <label for="manjokdo_cd2">만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd3" name="manjokdo_cd" type="radio" value="3">
	                                                <label for="manjokdo_cd3">보통</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd4" name="manjokdo_cd" type="radio" value="2">
	                                                <label for="manjokdo_cd4">불만족</label>
	                                            </span>
	                                            <span>
	                                                <input id="manjokdo_cd5" name="manjokdo_cd" type="radio" value="1">
	                                                <label for="manjokdo_cd5">매우불만족</label>
	                                            </span>
	                                        </li>
	                                        <li class="input">
	                                            <label for="gtuigyeon_cn" class="skip_label">의견 입력란</label>
	                                            <input id="gtuigyeon_cn" name="gtuigyeon_cn" value="" type="text" onfocus="gtuigyeonChk();" onblur="gtuigyeonChk();">
	                                            <span class="button middle gray3">
	                                                <input value="반영" type="button" onclick="manjokdoInsert()" class="btn_button">
	                                            </span>
	                                        </li>
	                                    </ul>
	                                </div>
	                                <div class="info">
	                                    <ul>
	                                        <li id="ddbuseo_nm"><strong>담당정보 : </strong>현역모집과</li>
	                                        <li id="ddjikwon_fnm"><strong>담당자명 : </strong>이병희(042-481-2748)</li>
	                                        <li id="cjdatabyeongyeong_dtm"><strong>자료기준 : </strong>2023-04-10</li>
	                                    </ul>
	                                </div>
	                            </div>
	                        </form>
	                        <!-- container -->
	                    </div>"""
html41="""<div id="contents">	                        
<div class="layout_h3">
<h3>기독교군종병(471277)/천주교군종병(471278)/불교군종병(471279)</h3>

<p>기독교군종병, 천주교군종병, 불교군종병은 성직업무보좌와 군종업무수행, 종교시설관리 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col" style="width: 750px; height: 394px;">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 4급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<br>
			(단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은 최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>자격기준(아래 항목 중 한가지 이상 해당자)
				<ul>
					<li>기독교군종병
					<ul>
						<li>관련 종교 전공학부(기독교학과, 신학과 또는 신학전공) 2년 재학 이상 또는 세례 받은 지 10년 이상자</li>
					</ul>
					</li>
					<li>천주교군종병
					<ul>
						<li>신학생 또는 영세 받은 지 5년 이상자로 본당신부 추천서 제출자
						<p>신학생 : 전국 가톨릭신학대학 및 대학원 신학과 재학 및 졸업생</p>
						</li>
					</ul>
					</li>
					<li>불교군종병
					<ul>
						<li>불교 관련 전공학과(불교학과) 1년 이상 수료자, 수계 받은 지 5년 이상자, 신앙생활 5년 이상자</li>
					</ul>
					</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>최종 학력증명서 1부(지원자격에 해당하는 자)</li>
	<li>세례, 영세, 수계증명서 1부(해당자만 제출)</li>
	<li>고교생활기록부 사본 1부</li>
	<li>본당 신부 추천서(해당자만 제출)</li>
	<li>종교활동증명서 1부(종교활동기간과 성직자가 자필 서명 또는&nbsp;종교기관 관인은 반드시 포함)
	<ul>
		<li>종교활동 : 목회,미사,법회 참여경력/성가대(반주포함)/학생회임원활동 등</li>
	</ul>
	</li>
	<li>자격증 사본 1부(해당자만 제출)</li>
	<li>지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</li>
</ul>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접평가 장소</h4>

<ul class="list">
	<li>면접장소 : 삼위일체 성당(충남 계룡시 신도안면 신도안1길 72)</li>
	<li>내비게이션 : 천주교 삼위일체 성당</li>
</ul>

<p>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내&nbsp; 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</p>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<p>최종선발은 서류전형 점수와 면접평가 점수를 합하여 고득점순으로 결정되며, 동점일 경우 면접평가 점수가 높은 순, 생년월일이 빠른 순으로 결정</p>

<p>입영일자는 배점기준에 따른 고득점자 순으로 입영희망월을 반영하여 결정</p>

<table class="table_col">
	<caption>서류심사, 면접에 대한 표이며 총점, 서류심사(1차), 면접(2차)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">총점</th>
			<th colspan="4" scope="colgroup">서류심사(1차)</th>
			<th rowspan="2" scope="col">면접(2차)</th>
		</tr>
		<tr>
			<th scope="col">종교활동</th>
			<th scope="col">전공학과</th>
			<th scope="col">고교출석률</th>
			<th scope="col">자격증</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td>10</td>
			<td>20</td>
			<td>10</td>
			<td>10</td>
			<td>50</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>종교활동</h5>

<table class="table_col">
	<caption>종교활동에 대한 표이며 구분, 10년 이상, 7년 이상, 5년 이상, 3년 이상, 1년 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">10년 이상</th>
			<th scope="col">7년 이상</th>
			<th scope="col">5년 이상</th>
			<th scope="col">3년 이상</th>
			<th scope="col">1년 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>점 수</td>
			<td>10</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
			<td>6</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공학과</h5>

<table class="table_col">
	<caption>전공학과에 대한 표이며 구분, 대학졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 고졸이하에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">대학졸업이상</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">전공학과</th>
			<td>20</td>
			<td>18</td>
			<td>17</td>
			<td>16</td>
			<td>15</td>
			<td rowspan="2">13</td>
		</tr>
		<tr>
			<th scope="row">비전공학과</th>
			<td colspan="5">13</td>
		</tr>
		<tr>
			<td colspan="7">
			<ul class="list">
				<li>전공학과
				<ul>
					<li>기독교 : 기독교 신학부(기독학과, 신학과, 신학전공)</li>
					<li>천주교 : 카톨릭대학교 신학과 또는 신학부</li>
					<li>불교 : 전국 4개대학(동국대, 동국대 경주캠퍼스, 금강대, 중앙승가대)&nbsp;불교학과, 응용불교학과, 불교학부, 불교학전공, 명상심리상담학과</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>고교출석률</h5>

<table class="table_col">
	<caption>고교출석률에 대한 표이며 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h5>자격증(분야별 높은 등급 1개 인정)</h5>

<table class="table_col">
	<caption>자격증에 대한 표이며 구분, 자격증 5개, 자격증 3개, 자격증 1개, 미보유에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">자격증 5개</th>
			<th scope="col">자격증 3개</th>
			<th scope="col">자격증 1개</th>
			<th scope="col">미보유</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">점 수</th>
			<td>10</td>
			<td>7</td>
			<td>4</td>
			<td>1</td>
		</tr>
		<tr>
			<th scope="row">자격증</th>
			<td colspan="4" rowspan="1"><!--StartFragment-->
			<p class="바탕글" style="text-align: center;">워드프로세스 2급이상, 컴퓨터활용능력 2급 이상, 문서실무사 2급 이상,<br>
			PCT(PC활용능력 평가시험) A.B, 사무자동화 산업기사, ITQ 지도사,<br>
			ITQ B등급 이상,&nbsp;&nbsp;E-test&nbsp;Professional&nbsp;워드 1급~3급,&nbsp;<br>
			&nbsp;E-test&nbsp;Professional&nbsp;엑셀 1급~3급,&nbsp;E-test&nbsp;Professional 파워포인트 1급~3급&nbsp;&nbsp;</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>면접평가</h5>

<table class="table_col">
	<caption>면접평가에 대한 표이며 계, 교리이해, 직무능력, 표현력, 국가관/가치관에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">계</th>
			<th scope="col">교리이해</th>
			<th scope="col">직무능력</th>
			<th scope="col">표현력</th>
			<th scope="col">국가관/가치관</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">50</th>
			<td>30</td>
			<td>10</td>
			<td>5</td>
			<td>5</td>
		</tr>
	</tbody>
</table>
</div>
※ 면접 합계점수 50점 중 60%(30점) 미만 취득자는&nbsp;선발제외 처리&nbsp;
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html42="""<div id="contents">                     
<div class="layout_h3">
<h3>군악병[양악(342.101),국악(342105),실용음악(342106)]</h3>

<p>군악병은 각종 의식행사 및 병영예술문화를 위한 연주활동 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 4급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<br>
			&nbsp;&nbsp;&nbsp; (단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은<br>
			&nbsp;&nbsp;&nbsp;&nbsp;최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>양악(목관, 금관, 타악, 현악), 실용음악(리드기타, 베이스기타, 음향, 컴퓨터음향, 가수, 피아노,올겐, 성악, 작곡&nbsp;&nbsp;등),<br>
			국악(관악, 현악, 무용, 성악, 타악, 작곡)경력자</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>실기평가 장소 : <strong><span style="color: rgb(255, 0, 0);">현재 음향, 작곡을 제외한 전 분야 영상평가 실시 중</span></strong></h4>

<ul class="list">
	<li>국방부 군악대(서울 동작구 국립현충원 내) → 지하철 4호선 동작역 하차&nbsp;&nbsp;
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>지원ㆍ실기평가 유의사항</h4>

<ul class="list">
	<li>모집하지 않는 악기지원자는 면접/실기평가를 받을 수 없음.</li>
	<li>실기평가 시 본인 신분증과 수험표를 지참하시기 바랍니다.</li>
</ul>

<p>실기평가는 무반주로 실시하되 본인 악기를 지참해야 합니다.(타악기, 피아노 제외)</p>
</div>

<div class="layout_h4">
<h4>지망 부대유형</h4>

<table class="table_col">
	<caption>지망 부대유형에 대한 표이며 계, 복무부대, 평가수전에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">계</th>
			<th scope="col">복무부대</th>
			<th scope="col">평가수준</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">50인조이상</th>
			<td>
			<ul class="list">
				<li>육군본부(대전)</li>
				<li>국방부(서울)</li>
				<li>육군사관학교(서울)</li>
				<li>수도방위사령부(서울)</li>
			</ul>
			</td>
			<td>
			<ul class="list">
				<li>목관, 금관, 타악기-음대재학 수준</li>
				<li>현악, 국악, 성악-해당분야 최고수준</li>
				<li>셋드럼-전문밴드수준</li>
				<li>평가방법
				<ul>
					<li>독주/ 협연 가능</li>
					<li>스네어 드럼, 마림바, 팀파니 연주가능</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">36인조이하</th>
			<td>
			<ul class="list">
				<li>지상작전사령부(경기)</li>
				<li>2작전사령부(대구)</li>
				<li>3사관학교(경북)</li>
				<li>특전사(경기)</li>
				<li>육군훈련소(충남)</li>
				<li>상무대(전남)</li>
				<li>학생군사학교(충북)</li>
				<li>부사관학교(전북)</li>
				<li>수도군단(경기)</li>
				<li>7군단(경기)</li>
				<li>52/56사단(경기)</li>
			</ul>
			</td>
			<td>
			<ul class="list">
				<li>목관, 금관, 타악기
				<ul>
					<li>음대입시 수준/ 그룹사운드 주자 수준</li>
					<li>중주, 행진곡/ 경음악 연주 가능</li>
					<li>관악기로써 의식곡/ 가요 연주 가능</li>
				</ul>
				</li>
				<li>현악, 국악, 성악
				<ul>
					<li>해당분야 고급수준</li>
					<li>Solo연주 가능</li>
				</ul>
				</li>
				<li>셋드럼 - 다양한 리듬 연주 수준</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h4>※ 위 모집부대를 제외한 사단급 군악대 군악병은 육군훈련소 및 사단급 신병교육대에 입소 후<br>
&nbsp;&nbsp; &nbsp;병력운영을 고려하여&nbsp;선발합니다.</h4>

<h3>선발배점 기준 및 악기별 평가항목</h3>
&nbsp; *&nbsp;초견곡 :&nbsp;미고지<br>
&nbsp;&nbsp;* 영상평가 시 초견곡은 생략될 수 있음<br>
면접(전 파트 공통)
<table style="width: 500px;">
	<tbody>
		<tr>
			<td style="text-align: center;">구&nbsp;&nbsp; 분</td>
			<td style="text-align: center;">평가항목</td>
			<td style="text-align: center;">배&nbsp; 점</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align: center;">면&nbsp;&nbsp; 접</td>
			<td style="text-align: center;">연주경력/지원동기/표현력</td>
			<td style="text-align: center;">5</td>
		</tr>
		<tr>
			<td style="text-align: center;">의지/정신력/용모/태도</td>
			<td style="text-align: center;">5</td>
		</tr>
		<tr>
			<td style="text-align: center;">계</td>
			<td style="text-align: center;">10</td>
		</tr>
	</tbody>
</table>
&nbsp;

<div class="layout_h5">
<h5>양악기</h5>

<table class="table_col">
	<caption>양악기에 대한 표이며 구분, 악기명, 평가기준, 배점, 비고에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">악기명</th>
			<th scope="col">평가기준</th>
			<th scope="col">배점</th>
			<th scope="col">비고</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="3" scope="row">목관악기<br>
			(양악)</th>
			<td rowspan="3">플루트, 클라리넷, 오보에, 바순, 색소폰</td>
			<td>초견곡</td>
			<td>30</td>
			<td class="text_left" rowspan="6">
			<ul class="list">
				<li>초견곡 : 당일제시</li>
				<li></li>
				<li>자유곡</li>
				<li>- 3분이상, 대학 입시곡 수준</li>
				<li></li>
				<li>스케일 : Major</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>자유곡</td>
			<td>50</td>
		</tr>
		<tr>
			<td>스케일(음계)</td>
			<td>10</td>
		</tr>
		<tr>
			<th rowspan="3" scope="row">금관악기<br>
			(양악)</th>
			<td rowspan="3">트럼펫, 트럼본, 바리톤, 호른, 튜바</td>
			<td>초견곡</td>
			<td>30</td>
		</tr>
		<tr>
			<td>자유곡</td>
			<td>50</td>
		</tr>
		<tr>
			<td>스케일(음계)</td>
			<td>10</td>
		</tr>
		<tr>
			<th rowspan="6" scope="row">타 악 기<br>
			(양악)</th>
			<td rowspan="3">세트드럼</td>
			<td>초견곡</td>
			<td>30</td>
			<td class="text_left">
			<ul class="list">
				<li>Snare Drum 연주</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>리 듬</td>
			<td>50</td>
			<td class="text_left">
			<ul class="list">
				<li>5가지 이상 : 8마디</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>기 타</td>
			<td>10</td>
			<td class="text_left">
			<ul class="list">
				<li>기타 타악기류</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td rowspan="3">팀파니/마림바/Snare</td>
			<td>초견곡</td>
			<td>30</td>
			<td class="text_left">
			<ul class="list">
				<li>당일제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>자유곡</td>
			<td>50</td>
			<td class="text_left">
			<ul class="list">
				<li>1분이상 연주</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>기 타</td>
			<td>10</td>
			<td class="text_left">
			<ul class="list">
				<li>팀파니 : 조율</li>
				<li>마림바: 스케일(Major)</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th rowspan="12" scope="row">실용음악</th>
			<td rowspan="2">피아노, 올갠</td>
			<td>초견곡</td>
			<td>30</td>
			<td class="text_left">
			<ul class="list">
				<li>당일제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>자유곡</td>
			<td>60</td>
			<td class="text_left">
			<ul class="list">
				<li>3분이상 연주, 대학 입시곡 수준</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td rowspan="2">작 곡</td>
			<td>편곡능력</td>
			<td>80</td>
			<td class="text_left">
			<ul class="list">
				<li>멜로디제시→관악곡으로 편곡</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>기악실기</td>
			<td>10</td>
			<td class="text_left">
			<ul class="list">
				<li>부전공 악기(피아노, 기타)</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td rowspan="2">성 악</td>
			<td>시창능력</td>
			<td>30</td>
			<td class="text_left">
			<ul class="list">
				<li>당일제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>자유곡</td>
			<td>60</td>
			<td class="text_left">
			<ul class="list">
				<li>가곡 1곡, 아리아 1곡</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td rowspan="2">가 수</td>
			<td>시창능력</td>
			<td>30</td>
			<td class="text_left">
			<ul class="list">
				<li>당일제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>자유곡</td>
			<td>60</td>
			<td class="text_left">
			<ul class="list">
				<li>대중가요 및 팝송 中 1곡</li>
				<li>팝페라&nbsp;가수 지원 가능</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td rowspan="2">리드기타, 베이스기타</td>
			<td>초견곡</td>
			<td>30</td>
			<td class="text_left">
			<ul class="list">
				<li>당일제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>자유곡</td>
			<td>60</td>
			<td class="text_left">
			<ul class="list">
				<li>가요 및 경음악 중 1곡</li>
				<li>에드립 16마디</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td rowspan="2">음 향</td>
			<td>이론 평가</td>
			<td>40</td>
			<td class="text_left">
			<ul class="list">
				<li>음향장비 전문적 지식평가</li>
				<li>사운드 디자인 작성</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>전공 실기</td>
			<td>50</td>
			<td>
			<ul class="list">
				<li>믹서, 녹음장비 사용</li>
				<li>시스템, 전원장비 설치</li>
				<li>자격 및 경력(증명서 지참)</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">현 악 기<br>
			(양악)</th>
			<td rowspan="2">바이올린,첼로, 비올라, 콘트라베이스</td>
			<td>초견곡</td>
			<td>30</td>
			<td>
			<ul class="list">
				<li>당일제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>자유곡</td>
			<td>60</td>
			<td class="text_left">
			<ul class="list">
				<li>3분이상 연주, 대학 입시곡 수준</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>국악기</h5>

<table class="table_col">
	<caption>국악기에 대한 표이며 구분, 평가기준, 배점, 비고에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th colspan="2" scope="col">평가기준</th>
			<th scope="col">배점</th>
			<th scope="col">비고</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="2" scope="row">대금, 피리, 가야금, 거문고, 아쟁, 해금</th>
			<td colspan="2">초견곡</td>
			<td>30</td>
			<td class="text_left">
			<ul class="list">
				<li>당일제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td colspan="2">자유곡</td>
			<td>60</td>
			<td class="text_left">
			<ul class="list">
				<li>산조, 정악 中 1곡</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th rowspan="3" scope="row">타 악</th>
			<td colspan="2">판 굿</td>
			<td>40</td>
			<td class="text_left">
			<ul class="list">
				<li>팀워크, 표현력, 연주자세</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td colspan="2">모듬북</td>
			<td>30</td>
			<td>
			<ul class="list">
				<li>곡구성, 퍼포먼스, 리듬감</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td colspan="2">기 타</td>
			<td>20</td>
			<td>
			<ul class="list">
				<li>사물놀이, 버나, 상모 등</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th rowspan="4" scope="row">국악작곡</th>
			<td colspan="2">정간보→5선보로 역보</td>
			<td>10</td>
			<td>
			<ul class="list">
				<li>당일제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td colspan="2">화성학 풀이</td>
			<td>40</td>
			<td class="text_left">
			<ul class="list">
				<li>Sop, Bass의 전통화성학 제시</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td colspan="2">곡 짓 기</td>
			<td>30</td>
			<td class="text_left">
			<ul class="list">
				<li>25현가야금, 장고를 포함한 3중주곡</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td colspan="2">기악실기</td>
			<td>10</td>
			<td class="text_left">
			<ul class="list">
				<li>부전공 악기 1종류 이상 연주</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">국악무용</th>
			<td colspan="2">창작작품</td>
			<td>40</td>
			<td class="text_left">
			<ul class="list">
				<li>1작품이상 시연</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td colspan="2">전통작품</td>
			<td>50</td>
			<td class="text_left">
			<ul class="list">
				<li>한량무, 살풀이, 훈령무, 승무 중</li>
				<li class="bd_text_02_3">1작품이상 시연</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th rowspan="4" scope="row">국악성악</th>
			<td rowspan="2">판소리</td>
			<td>자유곡</td>
			<td>40</td>
			<td class="text_left">
			<ul class="list">
				<li>5바탕 중 1곡</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>지정곡</td>
			<td>50</td>
			<td class="text_left">
			<ul class="list">
				<li>판소리 '춘향가' 中 사랑가</li>
				<li>'남도민요' 中 성주풀이</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td rowspan="2">민 요</td>
			<td>자유곡</td>
			<td>40</td>
			<td class="text_left">
			<ul class="list">
				<li>서도/경기민요 中 1곡</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>지정곡</td>
			<td>50</td>
			<td class="text_left">
			<ul class="list">
				<li>창부타령, 노랫가락, 방아타령</li>
				<li class="bd_text_02_3">12잡가 中 1곡</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html43="""<div id="contents">                       
<div class="layout_h3">
<h3>회계원가비용분석병 (331267)</h3>

<p>회계원가비용분석병은 무기 등 회계원가비용, 분석평가 관련 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>&nbsp;○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 4급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>자격기준(아래 항목 중 한가지 이상 해당자)</li>
				<li>4년제 대학(교) 재학 이상자로서 산업공학, 컴퓨터공학, 전기·전자공학, 기계공학 등 공학 관련 학과 및 경영학,&nbsp;경제학, 회계학, 통계학 등 유사학과 전공자</li>
				<li>공학 분야 기사 이상의 자격취득자</li>
				<li>공인회계사(국내,미국) 취득자</li>
			</ul>

			<p>위 지원자격 전공학과 석사학위 이상자 및 공인회계사(국내,미국), 공학 분야 기사 이상의 자격취득자 면접평가&nbsp;시 우대</p>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>서류</h5>

<ul class="list">
	<li>최종 학력증명서(재학, 졸업 등) 1부</li>
	<li>학위증명서 1부(해당자만 제출)</li>
	<li>고교생활기록부 사본 1부</li>
	<li>자격ㆍ면허증 사본 1부(해당자만 제출)</li>
	<li>지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</li>
</ul>

<p>지원서접수 및 전형일정</p>
</div>
</div>

<div class="layout_h4">
<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접/실기평가 장소</h4>

<ul class="list">
	<li>대전·충남지방병무청 모병면접실(대전 중구 중앙로16번길 5)
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<ul class="list">
	<li>최종선발은 서류전형 점수와 면접평가 점수를 합하여 고득점 순으로 결정됨.</li>
	<li>동점 시 선발기준 : 1차(생년월일이 빠른 순) / 최종(면접점수가 높은 순, 생년월일이 빠른 순)
	<ul>
		<li>※ 입영일자는 배점기준에 따른 고득점자부터 입영희망월을 반영하여 결정</li>
	</ul>
	</li>
</ul>

<table class="table_col">
	<caption>선발 및 평가에 대한 표이며 계, 1차(서류), 2차(면접)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">계</th>
			<th colspan="3" scope="colgroup">1차(서류)</th>
			<th scope="col">2차(면접)</th>
		</tr>
		<tr>
			<th scope="col">전공학과</th>
			<th scope="col">자격증</th>
			<th scope="col">고교출석률</th>
			<th scope="col">면접</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">100</th>
			<td>35</td>
			<td>10</td>
			<td>5</td>
			<td>50</td>
		</tr>
	</tbody>
</table>

<div class="layout_h5">
<h5>전공학과</h5>

<table class="table_row">
	<caption>전공학과에 대한 표이며 구분, 대학원 재학이상, 4년제 졸업, 3년수료(4년재학), 2년수료(3년재학), 1년수료(2년재학), 1년재학, 고졸이하에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_16p">
		<col class="width_12p">
		<col class="width_12p">
		<col class="width_12p">
		<col class="width_12p">
		<col class="width_12p">
		<col class="width_12p">
		<col class="width_12p">
	</colgroup>
	<tbody class="text_center">
		<tr>
			<th scope="row">구 분</th>
			<th>대학원<br>
			재학이상</th>
			<th>4년제 졸업</th>
			<th>3년수료<br>
			(4년재학)</th>
			<th>2년수료<br>
			(3년재학)</th>
			<th>1년수료<br>
			(2년재학)</th>
			<th>1년재학</th>
			<th>고졸이하</th>
		</tr>
		<tr>
			<th scope="row">직접학과</th>
			<td>35</td>
			<td>34</td>
			<td>33</td>
			<td>32</td>
			<td>31</td>
			<td>30</td>
			<td rowspan="3">27</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>33</td>
			<td>32</td>
			<td>31</td>
			<td>30</td>
			<td>29</td>
			<td>28</td>
		</tr>
		<tr>
			<th scope="row">기타학과</th>
			<td colspan="6">27</td>
		</tr>
	</tbody>
</table>

<h5>1. 직접학과 : 경영, 경제, 회계, 서무, 통계, 수학, 산업공학 계열<br>
2. 간접학과 : 컴퓨터공학, 전기전자공학, 기계공학 계열</h5>
</div>

<div class="layout_h5">
<h5>자격증</h5>

<table class="table_row">
	<caption>자격증에 대한 표이며 구분, 공인회계사, 공학분야기사에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_40p">
		<col class="width_40p">
	</colgroup>
	<tbody class="text_center">
		<tr>
			<th scope="row">구 분</th>
			<td>공인회계사</td>
			<td>공학분야기사</td>
		</tr>
		<tr>
			<th scope="row">배 점</th>
			<td>10</td>
			<td>5</td>
		</tr>
	</tbody>
</table>

<h5>고교출석률</h5>

<table class="table_row">
	<caption>고교출석에 대한 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_20p">
		<col class="width_20p">
		<col class="width_20p">
		<col class="width_20p">
	</colgroup>
	<tbody class="text_center">
		<tr>
			<th scope="row">구 분</th>
			<td>결석 0일</td>
			<td>결석 1~2일</td>
			<td>결석 3~5일</td>
			<td>결석 6일 이상</td>
		</tr>
		<tr>
			<th scope="row">배 점</th>
			<td>5</td>
			<td>4</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>

<h5>면접</h5>

<table class="table_row">
	<caption>면접에 대한 표이며, 구분, 국가관, 전공지식, 적극성, 논리력, 지원동기에 대한 정보 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_16p">
		<col class="width_16p">
		<col class="width_16p">
		<col class="width_16p">
		<col class="width_16p">
	</colgroup>
	<tbody class="text_center">
		<tr>
			<th scope="row">구 분</th>
			<th scope="row">국가관</th>
			<th scope="row">전공지식</th>
			<th scope="row">적극성</th>
			<th scope="row">논리력</th>
			<th scope="row">지원동기</th>
		</tr>
		<tr>
			<th scope="row">배 점</th>
			<td>10</td>
			<td>10</td>
			<td>10</td>
			<td>10</td>
			<td>10</td>
		</tr>
	</tbody>
</table>
</div>
</div>
&nbsp;* 면접점수 합계 50점 중 60%(30점) 미만 취득 시 선발 제외 처리
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html44="""<div id="contents">                           
<div class="layout_h3">
<h3>화생방시험병(211239), 생물학시험병(211298), 방사능분석연구보조병(211295)</h3>

<p>화생방시험병, 생물학시험병, 방사능분석연구보조병은 화생방에 관한 탐지, 표본수집, 방호책 실시분야 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 4급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<br>
			&nbsp;&nbsp;&nbsp;&nbsp; (단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>자격기준(아래 항목 중 한가지 이상 해당자)</li>
				<li>화생방시험병
				<ul>
					<li>공업화학산업기사 이상, 화공기사, 화학분석기사, 수질환경산업기사, 폐기물환경산업기사 이상 자격 취득한 사람</li>
					<li>화학분야 전공으로 2년 수료 이상인 사람</li>
				</ul>
				</li>
				<li>생물학시험병
				<ul>
					<li>의사, 수의사, 임상병리사 면허 취득한 사람</li>
					<li>생물학, 미생물분야 전공으로 2년 수료 이상인 사람</li>
				</ul>
				</li>
				<li>방사능분석연구보조병
				<ul>
					<li>RI감독면허, RI특수면허, RI일반면허, 방사선심사면허, 방사선사면허 취득한 사람</li>
					<li>원자력, 물리학, 방사선, 비파괴검사&nbsp;분야 전공으로 2년 수료 이상인 사람</li>
				</ul>
				</li>
			</ul>

			<p>※ 해당분야 3월 이상 경력자는 면접평가 시 우대</p>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람<br>
			○ 생물학시험병의 경우 색각이 이상 있는 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>최종 학력증명서(재학, 졸업 등) 1부</li>
	<li>자격ㆍ면허증 사본 1부(해당자만 제출)</li>
	<li>경력증명서 1부(해당자만 제출)</li>
	<li>영어어학성적표 사본(해당자만 제출, 서류 제출일 기준 2년 이내 성적만 유효함)</li>
	<li>국가유공자 자녀(독립유공자 손자녀) 증명서 1부(해당자만 제출)</li>
</ul>

<p>※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함.</p>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접평가 장소</h4>

<ul class="list">
	<li>국군화생방 방호사령부(서울 서초구 내곡동) ⇒ 양재전철역 7번출구에서 마을버스9번 승차하여 서초구청 예비군훈련장 하차
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>
<span style="font-size: 14px;">&nbsp;</span>

<div class="layout_h5">
<h5>최종선발은 서류전형 점수와 면접평가 점수를 합하여 고득점순으로 결정됨</h5>
* 동점 시 선발기준 : 면접점수가 높은 순, 생년월일이 빠른 순

<p>※ 입영일자는 배점기준에 따른 고득자점순, 입영희망월 순으로 결정</p>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한 표이며 모집특기, 총점, 서류,(60), 면접(50)에 대한 정보 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">모집특기</th>
			<th rowspan="2" scope="col">총점</th>
			<th colspan="3" scope="col">서류(60)</th>
			<th colspan="5" scope="col">면접(50)</th>
		</tr>
		<tr>
			<th scope="col">전공기간</th>
			<th scope="col">자격증</th>
			<th scope="col">가산점</th>
			<th scope="col">지원동기</th>
			<th scope="col">용모태도</th>
			<th scope="col">성장환경</th>
			<th scope="col">표현력</th>
			<th scope="col">직무능력</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>화생방</td>
			<td>100</td>
			<td>25</td>
			<td>17</td>
			<td>8</td>
			<td>10</td>
			<td>10</td>
			<td>9</td>
			<td>9</td>
			<td>12</td>
		</tr>
		<tr>
			<td>방사능분석</td>
			<td>100</td>
			<td>30</td>
			<td>10</td>
			<td>10</td>
			<td>8</td>
			<td>10</td>
			<td>8</td>
			<td>9</td>
			<td>15</td>
		</tr>
		<tr>
			<td>생물학</td>
			<td>100</td>
			<td>30</td>
			<td>10</td>
			<td>10</td>
			<td>8</td>
			<td>10</td>
			<td>8</td>
			<td>9</td>
			<td>15</td>
		</tr>
	</tbody>
</table>

<p>※ 자격증<br>
&nbsp; - 화생방시험병</p>

<table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">
	<tbody>
		<tr>
			<td rowspan="2">구분</td>
			<td rowspan="2">기사 이상</td>
			<td rowspan="2">산업기사</td>
			<td rowspan="2">기능사</td>
			<td colspan="2">일반자격증</td>
			<td rowspan="2">자격<br>
			미소지자</td>
		</tr>
		<tr>
			<td>1급<br>
			(기사 이상)</td>
			<td>2~3급<br>
			(기능사)</td>
		</tr>
		<tr>
			<td>직접</td>
			<td>17</td>
			<td>16</td>
			<td>15</td>
			<td>11</td>
			<td>10</td>
			<td>8</td>
		</tr>
		<tr>
			<td>유사</td>
			<td>15</td>
			<td>14</td>
			<td>13</td>
			<td>11</td>
			<td>10</td>
			<td>8</td>
		</tr>
		<tr>
			<td colspan="7">1. 직접 : 화공기술사(기사), 화학분석기사(기능사), 위험물기능장(산업기사, 기능사), 수질관리기술사, 수질환경기사(산업기사), 토양환경기술사(기사), 환경기능사, 폐기물처리기술사(기사, 산업기사), 화학물질 분석_L5(일학습병행, 기사급), 화학물질 취급관리_L3(일학습병행, 산업기사급), 화학물질 취급관리_L5(일학습병행, 기사급)<br>
			2. 유사&nbsp;: 생물공학기사,&nbsp;화약류제조기사(산업기사), 대기환경기사(산업기사), 생물분류기사(동물, 식물), 자연생태복원기사(산업기사), 농림토양평가관리산업기사, 환경영향평가_L5(일학습병행, 기사급)<br>
			3. 일반자격증 : MOS, 컴퓨터활용능력, 워드프로세서, 전산회계운용사, 한글속기, 정보기기운용기능사, 정보처리기능사<br>
			&nbsp;☞ MOS(microsoft office specialist) 자격증은 일반자격증 2~3급 점수 부여&nbsp;</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;- 생물학시험병</p>

<table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">
	<tbody>
		<tr>
			<td rowspan="2">구분</td>
			<td rowspan="2">기사 이상</td>
			<td rowspan="2">산업기사,<br>
			기능사</td>
			<td colspan="2">일반자격증</td>
			<td rowspan="2">자격<br>
			미소지자</td>
		</tr>
		<tr>
			<td>1급<br>
			(기사 이상)</td>
			<td>2~3급<br>
			(산업기사, 기능사)</td>
		</tr>
		<tr>
			<td>직접</td>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>6.5</td>
			<td>6</td>
		</tr>
		<tr>
			<td>유사</td>
			<td>8</td>
			<td>8</td>
			<td>7</td>
			<td>6.5</td>
			<td>6</td>
		</tr>
		<tr>
			<td colspan="7">1. 자격증 점수는 본인에게 유리한 자격증 1개만 적용 허용<br>
			2. 각 분야별 자격 종류<br>
			&nbsp; - 직접 :&nbsp;생명공학기술자격증(COBE), 생물공학기사, 식품기사, 위생사(산업기사로 인정),<br>
			&nbsp; - 유사 : 생물분류기사(동물, 식물), 자연생태복원기사, 인간공학기사, 수질환경기사, 토양환경기사, 폐기물처리기사<br>
			3. 일반자격증 : 컴퓨터활용능력, 워드프로세서, 정보처리기사, MOS(2~3급으로 인정) 등 국가공인자격증</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;- 방사능분석연구보조병</p>

<table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">
	<tbody>
		<tr>
			<td rowspan="2">구분</td>
			<td rowspan="2">기사 이상</td>
			<td rowspan="2">산업기사</td>
			<td rowspan="2">기능사</td>
			<td colspan="2">일반자격증</td>
			<td rowspan="2">자격<br>
			미소지자</td>
		</tr>
		<tr>
			<td>1급<br>
			(기사 이상)</td>
			<td>2~3급<br>
			(산업기사, 기능사)</td>
		</tr>
		<tr>
			<td>배점</td>
			<td>10</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
			<td>6.5</td>
			<td>3</td>
		</tr>
		<tr>
			<td colspan="8">1. 기사 이상 : 방사선관리기술사, 원자력기사, 원자력발전기술사, 핵연료기술사, 비파괴검사기사, RI(방사선동위원소)감독면서, RI특수면허, 핵연료물질취급면서(감독자), 방사선취급감독자면허, 원자로조종감독자면허, 비파괴검사관리_L5(일학습병행)<br>
			2. 산업기사&nbsp;: RI일반면허, 방사선심사면허, 비파괴검사산업기사, 핵연료물질취급면허(취급자), 원자로조종사면허, 방사선동위원소(일반), 비파괴검사관리_L3(일학습병행)<br>
			3. 기능사 : 방사선사 비파괴검사기능사<br>
			4. 일반자격증 : 컴퓨터활용능력, 워드프로세서, 정보처리기사, MOS(2~3급으로 인정) 등 기타 국가공인자격증<br>
			5. 높은 자격증 1개만 적용</td>
		</tr>
	</tbody>
</table>

<p><br>
※ 가산점 : 경력,&nbsp;영어우수자(TEPS&nbsp;, TOEIC, TOEFL), 국가유공자 자녀(독립유공자 손자녀 포함)<br>
※ 면접 점수 50점 중 30점 미만 취득 시 선발제외 처리</p>
</div>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html45="""<div id="contents">	                         
<div class="layout_h3">
<h3>정보보호병 (175104)</h3>

<p>정보보호병은 육군본부, 군단급, 전방의 일부사단에서 컴퓨터 정보보호관련 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상 등의 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>정보보호, 정보보안, 해킹방어 등 정보보호관련 학과 전공자</li>
				<li>국외·국내 정보보호 전문 자격증을 취득한 사람
				<ul>
					<li>국제공인정보시스템보안전문가(CISSP)</li>
					<li>사이버포렌식전문가(CCFP)</li>
					<li>정보보호관리사(CISM)</li>
					<li>정보시스템감시사(CISA)</li>
					<li>정보보안기사</li>
					<li>디지털포렌식전문가</li>
					<li>인터넷보안전문가</li>
					<li>정보보안관리사(ISM)</li>
					<li>해킹보안전문가</li>
					<li>정보보안산업기사</li>
					<li>디지털포렌식전문가2급</li>
					<li>인터넷보안전문가2급</li>
					<li>해킹보안전문가2급</li>
					<li>CCNA</li>
					<li>정보처리(기능사 이상)</li>
					<li>전자계산기(기능사 이상)</li>
					<li>전자계산기조직응용(기능사 이상)</li>
					<li>네트워크관리사</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>최종 학력증명서(재학, 졸업 등) 1부</li>
	<li>고교생활기록부 사본 1부</li>
	<li>자격증 사본 1부(해당자만 제출)</li>
	<li>경력증명서 1부(해당자만 제출)</li>
</ul>

<p>※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</p>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접평가 장소</h4>

<ul class="list">
	<li>대전·충남지방병무청 모병면접실 (대전 중구 중앙로 16번길 5 대전충남지방병무청 내)
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<div class="layout_h5">
<h5>1차 서류전형 2배수인원 선발 후 2차 면접평가를 실시함.</h5>

<ul class="list">
	<li>최종선발은 서류전형 점수와 면접평가 점수를 합하여 고득점 순으로 결정됨</li>
	<li>동점 시 선발기준 : 1차(생년월일이 빠른 순) / 최종(면접점수가 높은 순, 생년월일이 빠른 순)
	<ul>
		<li>입영일자는 배점기준에 따른 고득자점 순, 입영희망월 순으로 결정</li>
	</ul>
	</li>
</ul>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한 표이며 계, 서류심사(1차평가), 면접(2차평가)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">계</th>
			<th colspan="4" scope="col">서류심사(1차 평가)</th>
			<th>면접(2차 평가)</th>
		</tr>
		<tr>
			<th scope="col">전공학과</th>
			<th scope="col">고교출석률</th>
			<th scope="col">경력</th>
			<th scope="col">자격증</th>
			<th scope="col">직무지식, 표현력 등</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>100</td>
			<td>20</td>
			<td>10</td>
			<td>10</td>
			<td>20</td>
			<td>40</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>전공학과</h4>

<table class="table_col">
	<caption>전공학과에 대한 표이며 구분, 대학원이상, 4년제 졸업, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 고졸, 고졸미만에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">대학원<br>
			재학이상</th>
			<th scope="col">4년제<br>
			졸업</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸</th>
			<th scope="col">고졸미만</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">1순위</th>
			<td>20</td>
			<td>19</td>
			<td>17</td>
			<td>16</td>
			<td>14</td>
			<td>12</td>
			<td>10</td>
			<td rowspan="3">2</td>
		</tr>
		<tr>
			<th scope="row">2순위</th>
			<td>18</td>
			<td>16</td>
			<td>14</td>
			<td>12</td>
			<td>10</td>
			<td>8</td>
			<td>6</td>
		</tr>
		<tr>
			<th scope="row">비전공</th>
			<td>16</td>
			<td>14</td>
			<td>12</td>
			<td>10</td>
			<td>8</td>
			<td>6</td>
			<td>4</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>1순위 : 정보보호, 정보보안, 해킹방어 등 정보보호관련 학과</li>
	<li>2순위 : 컴퓨터공학, 전자계산학 관련학과, 전자공학, 정보통신, 통신, 전파 관련 학과</li>
</ul>
</div>

<div class="layout_h4">
<h4>고교출석률</h4>

<table class="table_col">
	<caption>고교출석률에 대한 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">점 수</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>경력</h4>

<table class="table_col">
	<caption>경력점수에 대한 표이며 계, 3년이상, 2~3년, 1~2년,&nbsp;차세대보안리더 양성프로그램(BOB)수료자에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">계</th>
			<th scope="col">3년이상</th>
			<th scope="col">2~3년</th>
			<th scope="col">1~2년</th>
			<th scope="col">차세대보안리더<br>
			양성프로그램(BOB)수료자</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>4</td>
			<td>3</td>
			<td>2</td>
			<td>6</td>
		</tr>
	</tbody>
</table>
&nbsp; * 정보보호업종 근무경력자<br>
&nbsp; * 공공기관(공무원) 정보보호직종 근무경력자
<div class="layout_h5">&nbsp; * BoB(Betst of the Best)인정기관 : 한국정보기술연구원</div>
</div>

<div class="layout_h4">
<h4>자격증</h4>

<table class="table_col">
	<caption>자격증에 대한 표이며 구분, 정보보호 전문 자격증, 정보보호 자격증, 정보보호 관련 자격증, 기본에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">정보보호<br>
			전문 자격증</th>
			<th scope="col">정보보호<br>
			자격증</th>
			<th scope="col">정보보호<br>
			&nbsp;관련 자격증</th>
			<th scope="col">기본</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">자격증</th>
			<td>국제공인정보시스템보안전문가(CISSP),<br>
			사이버포렌식전문가(CCFP),<br>
			정보보호관리사(CISM),<br>
			정보시스템감시사(CISA),<br>
			정보보안기사,<br>
			정보보안산업기사,<br>
			디지털포렌식전문가,<br>
			인터넷보안전문가,<br>
			정보보안관리사(ISM),<br>
			해킹보안전문가</td>
			<td>디지털포렌식전문가2급,<br>
			인터넷보안전문가2급,<br>
			해킹보안전문가2급, CHFI</td>
			<td>정보처리,<br>
			전자계산기,<br>
			전자계산기조직응용,<br>
			CCNA<br>
			네트워크관리사</td>
			<td></td>
		</tr>
		<tr>
			<th scope="row">배 점</th>
			<td>20</td>
			<td>18</td>
			<td>16</td>
			<td>10</td>
		</tr>
	</tbody>
</table>

<p>자격증 배점 : 자격등급이 높은 자격증 1개만 인정</p>
</div>

<div class="layout_h4">
<h4>면접</h4>

<table class="table_col">
	<caption>면접평가에 대한 표이며 구분, 지원동기, 면접태도, 대인관계역량, 표현력, 직무능력(필기시험)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">지원동기</th>
			<th scope="col">면접태도</th>
			<th scope="col">대인관계역량</th>
			<th scope="col">표현력</th>
			<th scope="col">직무능력<br>
			(필기시험)</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">40</th>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>20</td>
		</tr>
		<tr>
			<td colspan="6" style="text-align: left;">&nbsp;*1항목 이상 0점 평가 시 선발제외 처리</td>
		</tr>
	</tbody>
</table>
</div>
※ 면접평가는 반드시 정해진 평가일시 정각까지 참석바랍니다.<br>
&nbsp;&nbsp;&nbsp;(평가장소에 정해진 평가일시보다 늦게 도착할&nbsp;경우 평가 불가)<br>
&nbsp;&nbsp;&nbsp;<br>
&nbsp;&nbsp;
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html46="""<div id="contents">	            
<div class="layout_h3">
<h3>지형자료관리병 (161248) : <span style="color: rgb(255, 0, 0);"><strong>2023년 모집계획 없음</strong></span></h3>

<p>지형자료관리병은 장비를 이용하여 지형자료 분석분야의 임무를 수행합니다.</p>
</div>

<div class="layout_h4">
<h4>지원자격</h4>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 4급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<br>
			&nbsp;&nbsp;&nbsp;&nbsp; (단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>자격기준(아래 항목 중 한가지 이상 해당자)</li>
				<li>측량 및 지형공간 정보산업기사 이상, &nbsp;토목산업기사 이상, 지적산업기사 이상, 응용지질기사, 전자계산기산업기사 이상&nbsp;자격 취득자</li>
				<li>지리학, 지구학, 토목학, 지적학, 전산학 분야 전공으로 2년 수료 이상자</li>
				<li>GIS(지리정보시스템)관련업체 경력자 면접평가 시&nbsp;우대</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>○ 범죄경력 조회결과(경찰청)<br>
			- 징역 또는 금고의 형의 실형(집행유예 포함)을 선고 받은 사람<br>
			- 수사또는 재판중에 있는 사람<br>
			- 처분미상으로 통보된 사람<br>
			○ '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<p>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 안내 및 지원절차 → 육군 → 전문특기병 → 군사특기임무 및 설명을 클릭하면, 군사특기별 임무, 관련사진, 관련자격ㆍ면허ㆍ전공학과, 신체요건 등 군사특기에 관한 상세한 자료를 제공받을 수 있습니다.</p>
</div>

<div class="layout_h4">
<h4>구비서류</h4>

<div class="layout_h5">
<h5>제출할 서류</h5>

<ul class="list">
	<li>최종 학력증명서(재학, 졸업 등) 1부</li>
	<li>자격증 사본 1부(해당자만 제출)</li>
	<li>고교생활기록부 사본 1부</li>
	<li>경력증명서 1부(해당자만 제출)</li>
</ul>

<p>※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</p>
</div>
</div>

<div class="layout_h4">
<h4>지원서접수 및 전형일정</h4>

<dl class="list">
	<dt><a href="#" title="페이지 이동"><strong>접수 및 전형일정 알아보기(바로가기) : </strong></a></dt>
	<dd>병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 클릭하면, 모집 계획 및 전형일정에 대한 자료를 제공받을 수 있습니다.</dd>
</dl>
</div>

<div class="layout_h4">
<h4>면접평가 장소</h4>

<ul class="list">
	<li>대전·충남지방병무청 모병면접실(대전 중구 중앙로 16번길 5 대전충남지방병무청 내)
	<ul>
		<li>병무청과 육군 사정에 따라 접수, 전형 등 모집일정이 변경될 수 있사오니 정확한 모집일정은 병무청&nbsp;누리집 → 군지원(모병)안내 → 모집안내 서비스 → 이달의 모집계획 → 육군을 참조하시기 바랍니다.</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h4">
<h4>선발 및 평가 배점</h4>

<div class="layout_h5">
<h5>서류전형과 면접평가 점수를 합하여 고득점자 순으로 최종선발됨</h5>
<br>
* 동점 시 선발기준 :&nbsp;면접점수가 높은 순, 생년월일이 빠른 순
<p>※ 입영일자는 배점기준에 따른 고득자점순, 입영희망월 순으로 결정</p>

<table class="table_col">
	<caption>서류 및 면접에 대한 표이며 계, 서류, 면접 (직무지식,경력확인,지원동기 등)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">계</th>
			<th colspan="3" scope="col">서류</th>
			<th rowspan="2" scope="col">면접 (직무지식,경력확인,지원동기 등)</th>
		</tr>
		<tr>
			<th scope="col">전공학과</th>
			<th scope="col">자격증</th>
			<th scope="col">고교출석률</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td>100</td>
			<td>40</td>
			<td>30</td>
			<td>10</td>
			<td>20</td>
		</tr>
	</tbody>
</table>
</div>
&nbsp;&nbsp; *&nbsp;면접점수 20점 중 60%(12점) 미만 취득 시&nbsp;선발제외 처리&nbsp;

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<caption>전공에 대한 표이며 구분, 대학원재학이상, 4년제 졸업, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 고졸이하에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">대학원<br>
			재학이상</th>
			<th scope="col">4년제 졸업</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>40</td>
			<td>39</td>
			<td>37</td>
			<td>36</td>
			<td>35</td>
			<td>34</td>
			<td rowspan="3">28</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>37</td>
			<td>36</td>
			<td>35</td>
			<td>33</td>
			<td>32</td>
			<td>31</td>
		</tr>
		<tr>
			<th scope="row">기타학과</th>
			<td colspan="6">28</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>1. 직접학과 : 지리, 지적, 지형, 지구, 도시, 토목, 건설, 교통, 우주항공, 지역, 건축 계열<br>
2. 간접학과 : 전산, 컴퓨터, 전자공학, 정보 등 전산계열</h5>

<p>※ 환경공학, 환경학은 지원 비대상</p>
</div>

<div class="layout_h5">
<h5>자격증</h5>

<table class="table_col">
	<caption>자격증 배점 정보에 대한 표이며 구분, 기사이상, 산업기사, 기능에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">기사이상</th>
			<th scope="col">산업기사</th>
			<th scope="col">기능사</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>30</td>
			<td>25</td>
			<td>20</td>
		</tr>
		<tr>
			<th scope="row">자격증<br>
			명칭</th>
			<td>측량및지형공간정보기술사<br>
			토질및기초기술사, 토목기사<br>
			지적기사, 지적기술사<br>
			정자계산기사, 정보처리기사 등</td>
			<td>토목산업기사, 지적산업기사<br>
			측량 및 지형공간정보산업기사<br>
			전자계산기산업기사<br>
			정보처리산업기사 등</td>
			<td>토목제도기능사, 전산응용토목제도기능사,<br>
			지적기능사, 측량기능사, 지도제작기능사,<br>
			컴퓨터그래픽스운용기능사, 정보처리기능사,<br>
			전자계산기 및 캐드기능사, 컴퓨터운용사<br>
			워드프로세서 1/2/3급</td>
		</tr>
		<tr>
			<td colspan="4">&nbsp;* 자격등급이 높은 자격증 1개만 인정</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>고교출석률</h5>

<table class="table_col">
	<caption>고교출석률에 대한 점수표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">점 수</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html47="""<div id="contents">	                         
<div class="layout_h3">
<h3>신호정보/전자전운용 (152101)</h3>
</div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 4급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<br>
			&nbsp;&nbsp;&nbsp;&nbsp; (단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>수학, 암호학, 정보보호, 전기/전자, 정보통신, 컴퓨터공학, 전산학과 1학년 재학 이상인 사람</li>
				<li>제어계측, 로봇공학, 물리학, 통계학 1학년 재학 이상인 사람</li>
				<li>기사 (정보통신, 전파전자통신, 무선설비, 방송통신, 정보처리, 정보보안, 임베디드)를 취득한 사람</li>
				<li>산업기사 (정보통신, 전파전자통신, 무선설비, 방송통신, 정보처리, 정보 보안, 계측제어, 무선통신)를 취득한 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>
			<ul class="list">
				<li>범죄조회 결과 징역 또는 금고의 형의 실형(집행유예포함)을 선고 받은 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>청력장애, 디스크/관절이상, 운동장애, 폐결핵, 천식, 정신건강의학과 질환이 있는 사람</li>
				<li>&nbsp;'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<ul style="list-style-type: circle;">
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>
&nbsp;

<div class="layout_h3">
<h3>구비서류</h3>

<div class="layout_h4">
<h4>제출할 서류</h4>

<ul class="list">
	<li>최종학력(졸업,수료,휴학,퇴학,재학) 증명서 1부</li>
	<li>고등학교생활기록부 1부</li>
	<li>자격증 사본 1부(해당자)</li>
	<li>지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3>선발기준</h3>
</div>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차선발 : 서류심사평가 점수 고득점 순으로 계획인원 200% 선발
	<ul>
		<li>※ 동점 시에는 생년월일 빠른 순</li>
	</ul>
	</li>
	<li>최종선발 : 1차 평가와 2차 평가 합산하여 고득점 순 선발
	<ul>
		<li>※ 동점 시 면접평가 높은 순, 생년월일이 빠른 순 선발</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h3">
<h3>배점기준 총괄</h3>
&nbsp;

<table class="table_col">
	<caption>선발 및 평가 배점에 대한 내용표이며 계, 1차평가(서류심사), 2차평가(면접)에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th rowspan="2" scope="col">계</th>
			<th colspan="3" scope="col">1차 평가(서류심사)</th>
			<th colspan="1" rowspan="2" scope="col">2차 평가(면접)</th>
		</tr>
		<tr>
			<th scope="col">전공학과</th>
			<th scope="col">자격증</th>
			<th scope="col">고교출석률</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점(점)</th>
			<td>100</td>
			<td>40</td>
			<td>10</td>
			<td>10</td>
			<td>40</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>전공학과</h4>

<ul class="list">
	<li>직업전문학교(국가공인)은 대학교와 동일하게 인정</li>
</ul>

<table class="table_col">
	<caption>전공학과에 배점 표이며 구분, 대학원재학이상, 4년제 졸업, 2년수료/3년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학 고졸이하에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구 분</th>
			<th scope="col">대학원<br>
			재학이상</th>
			<th scope="col">4년제<br>
			졸업</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>40</td>
			<td>39</td>
			<td>38</td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td rowspan="3">25</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>35</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
			<td>28</td>
			<td>26</td>
		</tr>
		<tr>
			<th scope="row">기타학과</th>
			<td colspan="6">25</td>
		</tr>
	</tbody>
</table>

<h6>1. 직접학과 : 수학, 정보통신, 전기전자, 컴퓨터공학, 암호학, 정보보호, 전산학과 계열<br>
2. 간접학과 : 제어계측, 로봇공학, 물리학, 통계학 계열</h6>
</div>

<div class="layout_h4">
<h4>자격증</h4>

<table class="table_col">
	<caption>자격증에 대한 배점표이며 구분, 국가기술자격증(기사이상, 산업기사, 기능사), 기본에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th rowspan="2" scope="col">구분</th>
			<th colspan="3" scope="col">국가기술자격증</th>
			<th rowspan="2" scope="col">기본</th>
		</tr>
		<tr>
			<th colspan="1" scope="col">기사이상</th>
			<th colspan="1" scope="col">산업기사</th>
			<th colspan="1" scope="col">기능사</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">점수</th>
			<td>10</td>
			<td>9</td>
			<td>8</td>
			<td>5</td>
		</tr>
		<tr>
			<th colspan="1" scope="row">자격명칭</th>
			<td>정보통신,<br>
			전파전자통신,<br>
			무선설비,<br>
			방송통신,<br>
			정보처리,<br>
			정보보안,<br>
			임베디드,<br>
			산업계측제어</td>
			<td>정보통신,<br>
			전파전자통신,<br>
			무선설비,<br>
			방송통신,<br>
			정보처리,<br>
			정보보안</td>
			<td>전파전자통신,<br>
			무선설비,<br>
			방송통신,<br>
			정보처리</td>
			<td>-</td>
		</tr>
		<tr>
			<td colspan="5">※ 자격등급이 높은 자격증 1개만 인정</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>고교출석률</h4>

<table class="table_col">
	<caption>고교출석에 대한 배점표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상일에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th colspan="1" scope="col">구분</th>
			<th colspan="1" scope="col">결석 0일</th>
			<th colspan="1" scope="col">결석 1~2일</th>
			<th colspan="1" scope="col">결석 3~5일</th>
			<th colspan="1" scope="col">결석 6일 이상일</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>면접평가</h4>

<table class="table_col">
	<caption>면접평가에 대한 배점표이며 구분, 품성평가, 업무능령에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th scope="col">품성평가</th>
			<th scope="col">업무능력&nbsp;&nbsp;</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>15</td>
			<td>25</td>
		</tr>
	</tbody>
</table>
&nbsp;1) 면접평가 합계점수 40점 중 24점 이하 평가 시 선발제외 처리<br>
&nbsp;2) 품성평가 항목 15점 중 9점 이하 평가 시&nbsp;선발제외 처리<br>
&nbsp;*1), 2) 항목 중 1개라도 해당 시&nbsp;선발제외 처리&nbsp;&nbsp;</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html48="""<div id="contents">            
<div class="layout_h3">
<h3>S/W개발병 (175105)</h3>
<span style="font-size: 14px;">SW관리/개발, SW 운용간 보완사항에 대한 성능개량 임무를 수행합니다. &nbsp;</span></div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 4급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람<br>
			&nbsp;&nbsp;&nbsp;&nbsp; (단, 현역병지원 신체검사 결과 신체등급 4급인 경우 18세자는 신체등급 4급 현역복무 선택 동의한 경우, 19세 이상은<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 최종선발일 7일전까지 병역처분변경원을 신청하여 4급 보충역에서 4급 현역입영대상으로 처분이 변경된 경우에 입영가능)</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>전산, 컴퓨터, 소프트웨어, 인터넷, 전자계산, 정보보호, 전기·전자, 미디어, IT관련, 정보통신, 정보시스템&nbsp;관련학과 전공 2년 수료 이상자</li>
				<li>기사(정보처리, 전자계산기), 산업기사(정보처리, 전자계산기, 사무자동화), 기능사(정보처리, 전자계산기, 웹디자인), 게임프로그래밍전문가, SQLD(개발자), SW코딩자격(1~3급), COS PRO(1~3급)를 취득한 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>
			<ul class="list">
				<li>범죄조회 결과 징역 또는 금고의 형의 실형(집행유예포함)을 선고 받은 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>수지결손, 수지강직, 청력/언어 장애, 정신건강의학과 질환이 있는 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>
&nbsp;

<div class="layout_h3">
<h3>구비서류</h3>

<div class="layout_h4">
<h4>제출할 서류</h4>

<ul class="list">
	<li>최종학력(졸업,수료,휴학,퇴학,재학) 증명서 1부</li>
</ul>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 최종학력서류가 해외서류일 경우 한국어 번역공증서류 포함</p>

<ul class="list">
	<li>고등학교생활기록부 1부</li>
	<li>자격증 사본 1부(해당자)</li>
	<li>지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3>선발기준</h3>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차선발 : 서류심사평가 점수 고득점 순으로 계획인원 300% 선발
	<ul>
		<li>※ 동점 시에는 자격증 점수 높은 순, 전공학과 점수 높은 순, 생년월일 빠른 순</li>
	</ul>
	</li>
	<li>최종선발 : 1차 평가와 2차 평가 합산하여 고득점 순 선발
	<ul>
		<li>※ 동점 시에는 면접평가 높은 순, 자격증 점수 높은 순, 전공학과 점수 높은 순, 생년월일 빠른 순 선발</li>
	</ul>
	</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3>배점기준 총괄</h3>
&nbsp;<br>
&nbsp;
<table class="table_col">
	<caption>선발 및 평가 배점에 대한내용표이며 구분, 계, 1차 평가(서류심사), 2차평가(면접)에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구분</th>
			<th rowspan="2" scope="col">계</th>
			<th colspan="3" scope="col">1차 평가(서류심사)</th>
			<th colspan="1" rowspan="2" scope="col">2차 평가(면접)</th>
		</tr>
		<tr>
			<th scope="col">전공학과</th>
			<th scope="col">자격증</th>
			<th scope="col">고교출석률</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점(점)</th>
			<td>100</td>
			<td>20</td>
			<td>10</td>
			<td>10</td>
			<td>60</td>
		</tr>
	</tbody>
</table>

<div class="layout_h4">
<h4>전공학과</h4>

<ul class="list">
	<li>직업전문학교(국가공인)은 대학교와 동일하게 인정</li>
</ul>

<table class="table_col">
	<caption>전공학과에 대한 배점 표이며 구분, 대학원 재학이상, 4년제 졸업, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 고졸이하에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구 분</th>
			<th scope="col">대학원<br>
			재학이상</th>
			<th scope="col">4년제<br>
			졸업</th>
			<th scope="col">3년수료/<br>
			4년재학</th>
			<th scope="col">2년수료/<br>
			3년재학</th>
			<th scope="col">1년수료/<br>
			2년재학</th>
			<th scope="col">1년재학</th>
			<th scope="col">고졸이하</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>20</td>
			<td>19</td>
			<td>18</td>
			<td>17</td>
			<td>15</td>
			<td>13</td>
			<td rowspan="3">10</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>18</td>
			<td>17</td>
			<td>16</td>
			<td>15</td>
			<td>13</td>
			<td>11</td>
		</tr>
		<tr>
			<th scope="row">기타학과</th>
			<td colspan="6">10</td>
		</tr>
	</tbody>
</table>

<h6>1. 직접학과 : 전산, 컴퓨터, 소프트웨어, 전자계산 관련학과<br>
2. 간접학과 : 전기·전자, 정보통신, 정보시스템, 미디어, 인터넷, 정보보호,&nbsp;IT학 관련학과</h6>
</div>

<div class="layout_h4">
<h4>자격증</h4>

<table class="table_col">
	<caption>자격증에 대한 배점표이며 구분, 국내/국외공인자격증, 기본에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구분</th>
			<th colspan="3" scope="col">국내/국외 공인자격증</th>
			<th class="width_10p" rowspan="2" scope="col">기본</th>
		</tr>
		<tr>
			<th scope="col">기사이상 급</th>
			<th scope="col">산업기사 급</th>
			<th scope="col">기능사/일반자격증</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">점수</th>
			<td>10</td>
			<td>8</td>
			<td>6</td>
			<td>2</td>
		</tr>
		<tr>
			<th scope="row">국가<br>
			기술</th>
			<td>정보처리,<br>
			전자계산기,<br>
			&nbsp;</td>
			<td>정보처리,<br>
			전자계산기,<br>
			사무자동화,<br>
			<br>
			&nbsp;</td>
			<td>정보처리,<br>
			전자계산기,<br>
			웹디자인,&nbsp;<br>
			게임그래픽전문가,&nbsp;<br>
			SQL(개발자)<br>
			&nbsp;</td>
			<td>-</td>
		</tr>
		<tr>
			<th scope="row">민간<br>
			자격</th>
			<td>SW코딩자격 1급,<br>
			COS PRO 1급</td>
			<td>SW코딩자격 2급,<br>
			COS PRO 2급</td>
			<td>SW코딩자격 3급,<br>
			COS PRO 3급</td>
			<td>-</td>
		</tr>
		<tr>
			<th scope="row">일학습<br>
			병행</th>
			<td>디지털디자인_L5,<br>
			디지털디자인 디렉터_L6,<br>
			게임그래픽_L5,<br>
			게임 프로그래밍_L5,<br>
			전자기기소프트웨어개발_L5,<br>
			로봇소프트웨어 개발_L5,<br>
			SW개발_L5,<br>
			임베디드SW개발_L5-L6,<br>
			IT시스템우녕_L5,<br>
			SW테스트_L5<br>
			SW아키텍트_L5<br>
			IT프로젝트관리_L6</td>
			<td>디지털디자인_L3,<br>
			스마트 앱 디자인설계_L4,<br>
			전자기기소프트웨어개발_L4,<br>
			SW개발_L3</td>
			<td>전자기기소프트웨어개발_L2</td>
			<td>-</td>
		</tr>
		<tr>
			<td colspan="5">※ 자격등급이 높은 자격증 1개만 인정&nbsp;&nbsp;&nbsp;</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>고교출석률</h4>

<table class="table_col">
	<caption>고교출석에 대한 배점표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구분</th>
			<th scope="col">결석 0일</th>
			<th scope="col">결석 1~2일</th>
			<th scope="col">결석 3~5일</th>
			<th scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>면접평가</h4>

<table class="table_col">
	<caption>면접평가에 대한 배점표이며 구분, 지원동기, 면접태도, 표현력/적극성, 국가관/안보관, 직무수행능력에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구분</th>
			<th rowspan="2" scope="col">지원동기</th>
			<th rowspan="2" scope="col">면접태도</th>
			<th rowspan="2" scope="col">표현력/적극성</th>
			<th rowspan="2" scope="col">국가관/안보관</th>
			<th colspan="2" scope="col">직무수행능력</th>
		</tr>
		<tr>
			<th scope="col">SW개발상식<br>
			(질의/응답)</th>
			<th scope="col">SW개발 및<br>
			연수경력</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>10</td>
			<td>5</td>
			<td>5</td>
			<td>10</td>
			<td>20</td>
			<td>10</td>
		</tr>
	</tbody>
</table>
※ SW개발 및 연수 경력은 최고 10점까지 부여하고 해당 없을 시 기본점수 6점 부여,<br>
&nbsp;&nbsp; SW개발 근무와 연수경력 중복 시 높은 점수 부여<br>
&nbsp;1. SW개발 근무 경력자<br>
&nbsp;&nbsp; -&nbsp;근무경력은 한국소프트웨어산업협회 등록업체에 한해<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;근무기간 2년 이상(10점), 1년 이상 ~ 2년 미만(8점)<br>
✽ 경력증명서 및 한국소프트웨어산업협회 업체등록 근거를 면접 당일 제출<br>
&nbsp;2. 연수 경력자<br>
&nbsp; - 연수경력은 SW 마에스트로 연수과정자(선발자, 수료자)에 한해<br>
&nbsp;&nbsp;&nbsp; 6개월 수료(10점), 6개월 미만(8점)<br>
✽ SW 마에스트로 연수 선발 및 수료 증명서를 면접 당일 제출<br>
<br>
※ 면접평가 60점 중 40점 미만 취득 시 선발 제외 처리</div>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html49="""<div id="contents">                          
<div class="layout_h3">
<h3>드론운용및정비병 (156101)</h3>
<span style="font-size: 14px;">주기적으로 드론 상태 점검, 드론 및 통제장비 운용 ·정비 임무를 수행합니다.</span></div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 세부요건(전공학과, 자격증, 입상경력, 지원제한)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" colspan="2" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">기본요건</th>
			<td>○ 현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원한 사람<br>
			○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th rowspan="4" scope="row">세부요건</th>
			<th scope="row">전공학과</th>
			<td>
			<ul class="list">
				<li>관련 전공학과 1년 재학 이상인 사람</li>
				<li>관련 특성화고를 졸업한 사람</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 관련학과 : 드론, 무인항공기, 항공(조종, 정비, 기계 등), 로봇, 무인기 등 관련 전공&nbsp;</td>
		</tr>
		<tr>
			<th scope="row">자격증</th>
			<td>
			<ul class="list">
				<li>초경량비행장치(무인헬리콥터 1종, 2종/ 무인멀티콥터 1종, 2종/ 무인비행기 1종, 2종/무인비행선) 조종자 자격증을 취득한 사람</li>
			</ul>
			&nbsp;&nbsp;&nbsp; &nbsp; * 자격 차등화&nbsp;시행('21. 3. 1.) 이전 자격 취득자는 1종으로 인정&nbsp;<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* 발급기관 : 한국교통안전공단<br>
			&nbsp;&nbsp;&nbsp; &nbsp; * 사설업체 드론자격증은 인정하지 않음</td>
		</tr>
		<tr>
			<th scope="row">입상경력</th>
			<td>
			<ul>
				<li>접수마감일 기준 최근2년 이내 관련 대회에 입상한 사람</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *&nbsp;하단에 명시된 대회 및 종목에 입상한 사람에 한함</td>
		</tr>
		<tr>
			<th scope="row">지원제한</th>
			<td>
			<ul class="list">
				<li>범죄조회 결과 집행유예 이상의 범죄경력사실이 있는 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>수지결손, 수지강직, 시각장애, 수전증, 청각장애, 색각장애, 정신건강의학과 질환이 있는 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>
&nbsp;

<div class="layout_h3">
<table class="table_col">
	<caption>전공학과에 대한 내용표이며 관련 인정대회 및 종목 명단에 대한 내용을 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">&nbsp;관련 인정대회 및 종목 명단&nbsp;&nbsp;&nbsp;&nbsp;</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<td style="text-align: left;">
			<div style="text-align: left;">[1] 육군 참모총장배 드론경연대회(육군본부 / 드론축구, 클레수, 드론레이싱 종목)<br>
			[2] 2셀 FPV 드론 레이싱 대회(수성대학교 / 드론 레이싱 종목)<br>
			[3] 태조 청소년 드론레이싱 대회(충남·천안시 / 드론 레이싱 종목)<br>
			[4] 호남권 드론축구 대회((사)대한드론축구협회 / 드론축구 종목)<br>
			[5] 경북도지사배 국제드론축구 대회(경북·김천시 / 드론축구 종목)<br>
			[6] FPV/VR 미니 드론 레이싱 대회(문화체육관광부 / 드론 레이싱 종목)<br>
			[7] 국토부장관배 전국드론 축구대회(국토부 / 드론축구 종목)<br>
			[8] 세계일보 전국드론축구대회(세계일보 / 드론축구 종목)<br>
			[9] 보은 대추배 드론레이싱 대회(충북·보은군 / 드론레이싱 종목)<br>
			[10] 대구드론페스타(대구MBC / 드론레이싱, 축구 종목)<br>
			[11] 한국국토정보공사 전국 드론축구대회(한국국토정보공사 / 드론축구 종목)<br>
			[12] Spoex 전국드론축구대회(전주시 / 드론축구 종목)<br>
			[13] 유소년 전국 드론 축구 대회(사천시 / 드론축구 종목)<br>
			[14] 정읍 드론 페스티벌(정읍시 / 드론레이싱, 드론축구 종목)<br>
			[15] 공군참모총장배 드론 종합경연 대회(공군본부 / 드론축구 종목)<br>
			[16] 전국 드론 사진·영상 공모전(충청북도 / 영상 종목)<br>
			[17] 춘천 드론페스티벌 드론축구대회(춘천시 / 드론축구 종목)<br>
			[18] 춘천 레저컵 드론레이싱 대회(춘천시 / 드론레이싱 종목)<br>
			[19] D1 FPV 레이싱 대회(드로젠 주식회사 / 드론레이싱 종목)<br>
			[20] 울산 청소년 드론레이싱 대회(울산광역시 / 드론레이싱 종목)<br>
			[21] K-드론 월드 그랑프리(K-드론협회 / 드론레이싱 종목)<br>
			[22] 코리아 드론축구 페스티벌(전주시 / 드론축구 종목)<br>
			[23] 고양 드론축구 챔피언십 리그(고양시 / 드론축구 종목)<br>
			[24] 전국 드론축구대회(구미시 / 드론축구 종목)<br>
			[25] 강원컵 전국드론축구 대회(강원·영월군 / 드론축구 종목)<br>
			[26] 전북 지부장배 전라권 드론축구대회(전주시 / 드론축구 종목)<br>
			[27] 세계일보 전국드론 축구대회(세계일보 / 드론축구)<br>
			[28] 대한 드론축구협회장배 전국드론 축구대회((사)대한드론축구협회 / 드론축구 종목)<br>
			[29] 영월 DSI 국제 드론스포츠 챔피언십(강원, 영월 / 드론레이싱 종목)<br>
			[30] 청라 로봇랜드 드론레이싱대회(인천광역시 / 드론레이싱 종목)<br>
			[31] 정서진 드론페스티벌((사)한국코딩 드론메이커스 / 드론레이싱 종목)<br>
			[32] 드론페스티벌-드론레이스대회(인천광역시 / 드론레이싱 종목)<br>
			[33] 세종특별자치시 청소년 드론대회(세종시 / 드론레이싱 종목)<br>
			[34] 대전 드론챌린지(대전시 / 드론미로찾기 종목)<br>
			[35] 대한민국 드론산업 민간기능경기대회(KTC 사회적협동조합 / 장애물비행 종목)<br>
			[36] 충청권 드론축구대회(충남정보문화원 / 드론축구 종목)<br>
			[37] 국토부장관배 전국드론축구대회(국토부장관/전주시 / 드론축구 종목)<br>
			[38] 전북미래과학 체험전 새만금 로봇&amp;드론경진대회(군산시 / 드론레이싱 종목)<br>
			[39] 울산 드론미션대회(경상일보, 울산시 / 드론축구 종목)<br>
			[40] 부산청소년드론대회(부산시 / 드론 장애물 회피 비행 종목)<br>
			[41] 세계 비스드론대회 (미국)(탐지, 조종 분야 종목)<br>
			[42] 산업드론챔피언십(한국교통안전공단 / 조종기량부분(촬영 및 편집) 종목)<br>
			[43] 전국드론사진 영상 공모전(충청북도 / 영상 부분 종목)<br>
			[44] 소래생태습지공원 드론 항공촬영 경연대회(남동구 / 드론 항공촬영 종목)<br>
			[45] 드론클레쉬 캠퍼스리그(한국대학드론스포츠협의회 / 드론클레쉬 종목)<br>
			[46] 사천에어쇼 공군참모총장배 드론클레쉬(공군본부 / 드론클레쉬 종목)<br>
			[47] 광주시 빛고을 드론페스티벌(전남·광주시 / 드론축구, 클레쉬, 영상 종목)<br>
			[48] 광주시의회 의장배 전국 FPV 드론레이싱 단일대회(광주시 / 드론레이싱 종목)<br>
			[49] 드론영상, 사진 공모전(경기콘텐츠진흥원 / 드론영상 종목)<br>
			[50] 과천 드론레이싱 챔피언십(과천시체육회 / 드론레이싱 종목)<br>
			[51] 밀양 드론페스티벌(밀양시청, 대경대학교 / 드론영상 종목)<br>
			[52] 경남 고성 드론페스티벌(경남 고성군, 경남테크노파크 / 드론레이싱 종목)<br>
			[53] 전국기능경기대회 산업용 드론제어(대전광역시/드론제작 및 GCS구성, 비행제어 종목)</div>
			</td>
		</tr>
	</tbody>
</table>

<h3><strong><span style="color: rgb(0, 0, 255);">&nbsp;* 입상경력 인정대회 관련 문의 :&nbsp;042-550-3521(육군본부)</span></strong><br>
<br>
제출서류</h3>

<table class="table_col">
	<caption>제출서류에 대한 표이며 구분, 내용에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">필 수</th>
			<td>
			<ul>
				<li>고교생활기록부 1부</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">해당자</th>
			<td>
			<ul class="list">
				<li>최종학력(졸업, 수료, 휴학, 퇴학, 재학) 증명서 1부</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>* 최종학력서류가 해외서류일 경우 한국어 번역공증서류 포함</strong>

			<ul class="list">
				<li>자격증 사본(앞면,&nbsp;뒷면)&nbsp;1부</li>
				<li>입상 경력증명서 1부, 대회공고문 1부 → 반드시 주관단체 발행 "입상경력증명서"로 제출</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<p>&nbsp; * 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함<br>
&nbsp;</p>

<h3>선발기준</h3>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차선발 : 서류심사평가 점수 고득점 순으로 계획인원 200% 선발</li>
	<li>최종선발 : 1차 평가와 2차 평가 합산하여 고득점 순 선발</li>
	<li>동점 시&nbsp;선발기준 : 면접실기 점수가 높은 순 - 입상경력 점수가 높은 순 - 전공점수가 높은 순 - 자격점수가 높은 순 - 생년월일이 빠른 순 선발</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3>배점기준 총괄</h3>

<table class="table_col">
	<caption>선발 및 평가 배점에 대한 배점표이며 구분, 계, 1차평가(서류심사), 2차평가(면접/실무평가)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_10p" rowspan="2" scope="col">계</th>
			<th class="width_60p" colspan="4" scope="col">1차 평가(서류심사)</th>
			<th class="width_15p" rowspan="2" scope="col" style="text-align: left;">2차평가<br>
			(면접/실무평가)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
		</tr>
		<tr>
			<th class="width_20p" scope="col">전공학과</th>
			<th class="width_20p" scope="col">자격증</th>
			<th class="width_20p" scope="col">고교<br>
			출석률</th>
			<th class="width_20p" scope="col" style="text-align: left;">입상경력</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>100</td>
			<td>15</td>
			<td>15</td>
			<td>10</td>
			<td>10</td>
			<td>50</td>
		</tr>
	</tbody>
</table>

<div class="layout_h4">
<h4>전공학과</h4>

<table class="table_col">
	<caption>전공학과에 대한 배점 표이며, 구분, 4년제 졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1~2년 재학/특성화고 졸업, 비전공에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_14p" scope="col">4년제<br>
			졸업 이상</th>
			<th class="width_14p" scope="col">3년 수료/<br>
			4년 재학</th>
			<th class="width_14p" scope="col">2년 수료/<br>
			3년 재학</th>
			<th class="width_14p" scope="col">1~2년 재학/<br>
			특성화고 졸업</th>
			<th class="width_14p" scope="col">&nbsp;비전공</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>15</td>
			<td>14</td>
			<td>13</td>
			<td>12</td>
			<td>10</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>관련학과 : 드론, 무인항공기, 항공(조종, 정비, 기계 등), 로봇, 무인기 등 관련 전공&nbsp;</li>
</ul>
</div>

<div class="layout_h4">
<h4>자격증</h4>

<table class="table_col">
	<caption>자격증에 대한 배점 표이며 구분,&nbsp;경량비행장치 조종자 자격증(한국교통공단)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th colspan="5" scope="col" style="text-align: left;">ㅇ 초경량비행장치 조종자 자격증(한국교통공단)<br>
			&nbsp; - 무인헬리콥터/무인멀티콥터/무인비행기/무인비행선</th>
		</tr>
		<tr>
			<th rowspan="2" scope="col">등수</th>
			<th rowspan="2" scope="col">실기평가 조종자</th>
			<th rowspan="2" scope="col">지도 조종자</th>
			<th colspan="2" scope="col">기본 조종자</th>
			<th rowspan="2" scope="col">미취득</th>
		</tr>
		<tr>
			<th scope="col">1종</th>
			<th scope="col">2종</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>15</td>
			<td>13</td>
			<td>10</td>
			<td>8</td>
			<td>5</td>
		</tr>
		<tr>
			<td colspan="6" style="text-align: left;">
			<p style="text-align: justify;">* 국토부(한국교통안전공단)에서 발급한 자격증 및 교육과정 이수증(지도/실기평가조종자) 제출<br>
			* 기본 조종자의 경우&nbsp;1종 및 2종 자격증만 인정(3종 이하 자격증 미인정)<br>
			* 기본 조종자의 경우 자격 차등화 시행('21.3.1.) 이전 자격 취득자는 1종으로 인정<br>
			* 자격 차등화가 적용되지 않는 무인비행선 기본 조종자 취득자의 경우 1종 점수 부여<br>
			* 자격증 제출 시 앞면, 뒷면 사본 제출<br>
			* 사설업체 드론자격증은 미인정&nbsp;</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>고교출석률</h4>

<table class="table_col">
	<caption>고교출석에 대한 배점표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상일에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_20p" scope="col">결석 0일</th>
			<th class="width_20p" scope="col">결석 1~2일</th>
			<th class="width_20p" scope="col">결석 3~5일</th>
			<th class="width_25p" scope="col">결석 6일 이상일</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>10</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
		</tr>
		<tr>
			<td class="text_left" colspan="5">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>

<h4>&nbsp;입상경력</h4>

<table class="table_col">
	<caption>입상경력에 대한 배점 표이며 구분, 입상횟수, 기본점수에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th scope="col">구분</th>
			<th colspan="4" scope="col">입상횟수</th>
			<th rowspan="2" scope="col">기본<br>
			점수</th>
		</tr>
		<tr>
			<th scope="col">등수</th>
			<th scope="col">10회 이상</th>
			<th scope="col">6~9회</th>
			<th scope="col">3~5회</th>
			<th scope="col">1~2회</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>10</td>
			<td>8</td>
			<td>6</td>
			<td>4</td>
			<td>2</td>
		</tr>
		<tr>
			<td colspan="6" style="text-align: left;">
			<p style="text-align: justify;">※&nbsp;1. 접수마감일 기준 최근 2년 이내의 대회에 한함<br>
			&nbsp;&nbsp; &nbsp;2.&nbsp;상단에 명시된 대회의 해당 종목의 입상자에 한하며 성인용 종목에 한함<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 대회 공고문(전국대회 증명용) 1장, 입상경력증명서 제출<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; → 반드시 주관단체 발행 "입상경력증명서"로 제출(상장 사본&nbsp;미인정)&nbsp;</p>
			</td>
		</tr>
	</tbody>
</table>
</div>
</div>
&nbsp;

<div class="layout_h3">
<h3>면접/실무평가</h3>

<table class="table_col">
	<caption>면접 및 실무평가에 대한 배점표이며 계, 지원동기, 면접태도, 표현력/적극성, 국가관/안보관, 직무수행 능력(드론조종능력)에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_12p" scope="col">계</th>
			<th class="width_12p" scope="col">지원동기</th>
			<th class="width_12p" scope="col">면접<br>
			태도</th>
			<th class="width_12p" scope="col">표현력/<br>
			적극성</th>
			<th class="width_12p" scope="col">국가관/<br>
			안보관</th>
			<th class="width_15p" scope="col">직무수행 능력<br>
			(드론조종능력)</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>50</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>30</td>
		</tr>
		<tr>
			<td class="text_left" colspan="7">* 1개 항목이라도 0점 배점 시&nbsp;선발제외 처리<br>
			* 실기평가는 우천 등 기상악화로 제한될 경우 시뮬레이터를 활용하여 평가</td>
		</tr>
	</tbody>
</table>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html50="""<div id="contents">	                         
<div class="layout_h3">
<h3>영상콘텐츠디자이너 (341335)</h3>
<!-- <span style="font-size: 14px;">주기적으로 드론 상태 점검, 드론 및 통제장비 운용 &middot;정비 임무를 수행합니다.</span></div> --></div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 세부요건(전공학과, 기타), 지원제한에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" colspan="2" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">세부요건<br>
			(中1)</th>
			<th scope="row">전공학과</th>
			<td>
			<ul class="list">
				<li>영상콘텐츠제작과, 방송광고제작과, CF제작과, 디지털 콘텐츠과 등 영상관련학과 1년 수료 이상인 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">기타</th>
			<td>
			<ul class="list">
				<li>영상 분야 실무경력이&nbsp;15개월 이상인 사람</li>
				<li>고등학교(특성화고, 특목고 등)&nbsp;관련학과를 졸업한 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">지원제한</th>
			<td>
			<ul class="list">
				<li>범죄조회 결과 집행유예 이상의 범죄경력사실이 있는 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능&nbsp;</li>
</ul>
</div>

<div class="layout_h3">
<h3>제출서류</h3>

<table class="table_col">
	<caption>제출서류에 대한 표이며 구분, 내용에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">필 수</th>
			<td>
			<ul class="list">
				<li>최종학력(졸업, 수료, 휴학, 퇴학, 재학) 증명서 1부</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;<strong>* 최종학력서류가 해외서류일 경우 한국어 번역공증서류 포함</strong></td>
		</tr>
		<tr>
			<th scope="row">해당자</th>
			<td>
			<ul class="list">
				<li>영상 분야 실무경력 증명서 사본 1부</li>
				<li>영상 관련 고등학교 졸업 증명서 1부</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3><span style="font-size: 12px;">※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</span><br>
<br>
선발기준</h3>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차 선발 : 서류심사평가 점수 고득점 순으로 계획인원 500% 선발<br>
	<strong>* 동점 시에는&nbsp;생년월일이 빠른 순으로 선발</strong></li>
	<li>2차 선발 : 1차 선발인원 대상, 포트폴리오·실기평가, 면접 시행</li>
	<li>최종 선발 : 1차 평가점수와 무관하게, 2차 평가 고득점 순으로 선발<br>
	<strong>* 동점 시에는 생년월일이 빠른 순으로 선발</strong></li>
</ul>
</div>

<div class="layout_h4">
<h4>배점기준 총괄</h4>
&nbsp;

<table class="table_col">
	<caption>선발 및 평가 배점에 대한 배점표이며 계, 1차평가, 2차평가에 대한내용을 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_10p" rowspan="2" scope="col">계</th>
			<th class="width_60p" colspan="3" scope="col">1차 평가</th>
			<th class="width_15p" rowspan="2" scope="col">2차 평가</th>
		</tr>
		<tr>
			<th class="width_20p" scope="col">전공학과</th>
			<th class="width_20p" scope="col">실무경력</th>
			<th class="width_20p" scope="col">고교출석률</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>100</td>
			<td>15</td>
			<td>25</td>
			<td>10</td>
			<td>50</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>1차 평가</h4>

<div class="layout_h5">
<h5>전공학과</h5>

<table class="table_col">
	<caption>전공학과에 대한 배점 표이며 구분, 4년제 졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 영상관련특성화고 졸업자, 비전공에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_12p" scope="col">4년제<br>
			졸업이상</th>
			<th class="width_12p" scope="col">3년수료/<br>
			4년재학</th>
			<th class="width_12p" scope="col">2년수료/<br>
			3년재학</th>
			<th class="width_12p" scope="col">1년수료/<br>
			2년재학</th>
			<th class="width_12p" scope="col">1년재학</th>
			<th class="width_13p" scope="col">고등학교<br>
			관련학과<br>
			졸업자</th>
			<th class="width_12p" scope="col">비전공</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>15</td>
			<td>13</td>
			<td>11</td>
			<td>10</td>
			<td>9</td>
			<td rowspan="2">13</td>
			<td rowspan="2">6</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>13</td>
			<td>11</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
		</tr>
		<tr>
			<th scope="row">비 고</th>
			<td colspan="7">고등학교 관련학과 졸업자가 대학을 진학 했을 경우, 높은 점수 1개만 인정</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>1. 직접학과 : 영상·CF·영화 등 관련 학과</li>
	<li>2. 간접학과 : 언론·홍보·방송 등 관련 학과</li>
</ul>
</div>

<div class="layout_h5">
<h5>실무경력</h5>

<table class="table_col">
	<caption>실무경력에 대한 표이며 구분, 경력없음/1개월 미만/1개월~15개월까지 3개월 단위로 달라지는 배점 안내</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_12p" scope="col">15개월<br>
			이상</th>
			<th class="width_12p" scope="col">12개월~<br>
			15개월<br>
			미만</th>
			<th class="width_12p" scope="col">9개월~<br>
			12개월<br>
			미만</th>
			<th class="width_12p" scope="col">6개월~<br>
			9개월<br>
			미만</th>
			<th class="width_12p" scope="col">3개월~<br>
			6개월<br>
			미만</th>
			<th class="width_13p" scope="col">1개월~<br>
			3개월<br>
			미만</th>
			<th class="width_12p" scope="col">1개월<br>
			미만</th>
			<th class="width_12p" scope="col">경력<br>
			없음</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">25</td>
			<td style="text-align: center;">23</td>
			<td style="text-align: center;">21</td>
			<td style="text-align: center;">19</td>
			<td style="text-align: center;">17</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: center;">13</td>
			<td style="text-align: center;">11</td>
		</tr>
		<tr>
			<th scope="row">비 고</th>
			<td colspan="8" style="text-align: justify;">&nbsp; 회사명의 경력증명서 제출(범위제한 없음)<br>
			&nbsp;&nbsp; * 2차 평가 시 재직여부 확인, 허위로 밝혀질 경우 선발제외</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5><br>
고교출석률</h5>

<table class="table_col">
	<caption>고고출석률에 대한 배점 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_17p" scope="col">결석 0일</th>
			<th class="width_17p" scope="col">결석 1~2일</th>
			<th class="width_17p" scope="col">결석 3~5일</th>
			<th class="width_17p" scope="col">결석 6일 이상&nbsp;</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>2차 평가</h4>

<table class="table_col">
	<caption>2차 평가에 대한 배점 표이며, 구분, 면접, 직무수행능력(실기평가), 포트폴리오에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_45p" colspan="3" scope="col">면&nbsp;접</th>
			<th class="width_25p" rowspan="2" scope="col">직무수행능력<br>
			(실기평가)</th>
			<th class="width_15p" rowspan="2" scope="col">포트폴리오</th>
		</tr>
		<tr>
			<th class="width_15p" scope="col">면접태도</th>
			<th class="width_15p" scope="col">표현력/적극성</th>
			<th class="width_15p" scope="col">국가관/안보관</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>30</td>
			<td>5</td>
		</tr>
		<tr>
			<td class="text_left" colspan="6">* 직무수행능력평가 : 기획력, 영상촬영 및 편집(프리미어 및 에프터 이펙트 활용)<br>
			&nbsp; - 직무수행능력평가 항목은 평가주관부대 사정에 따라 변경될 수 있음<br>
			* 포트폴리오 : 개인 출품작, 유튜브 등 인터넷 사이트 탑재작(Master 파일)<br>
			* 1개 항목이라도 0점 배점 시 불합격</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h3">
<h3>전공학과 목록</h3>

<table class="table_col">
	<caption>전공학과 목록 표이며 직접관련학과, 간접관련학과에 대한 정보를 제공</caption>
	<tbody>
		<tr>
			<th class="width_15p" scope="row">직접관련 학과</th>
			<td class="width_85p">영상콘텐츠제작과, 방송광고제작과, CF제작과 등 ‘영상’, ‘광고’, ‘CF’, '영화' 가 포함된 학과</td>
		</tr>
		<tr>
			<th class="width_15p" scope="row">간접관련 학과</th>
			<td class="width_85p">신문방송학과, 언론홍보학과 등 ‘신문’, ‘언론’, ‘홍보’, ‘방송’, ‘미디어’, '디자인'이 포함된 학과</td>
		</tr>
	</tbody>
</table>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html51="""<div id="contents">	                          
<div class="layout_h3">
<h3>그래픽디자이너 (341336)</h3>
<!-- <span style="font-size: 14px;">주기적으로 드론 상태 점검, 드론 및 통제장비 운용 &middot;정비 임무를 수행합니다.</span></div> --></div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 세부요건(전공학과, 기타), 지원제한에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" colspan="2" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">세부요건<br>
			(中1)</th>
			<th scope="row">전공학과</th>
			<td>
			<ul class="list">
				<li>광고·멀티미디어디자인과, 디지털그래픽디자인과, 웹디자인과 등 1년 수료 이상인 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">기타</th>
			<td>
			<ul class="list">
				<li>디자인 분야 실무경력이&nbsp;15개월 이상인 사람</li>
				<li>고등학교(특성화고, 특목고 등)&nbsp;관련학과를 졸업한 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">지원제한</th>
			<td>
			<ul class="list">
				<li>범죄조회 결과 집행유예 이상의 범죄경력사실이 있는 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<div class="layout_h3">
<h3>제출서류</h3>

<table class="table_col">
	<caption>제출서류에 대한표이며 구분, 내용에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">필 수</th>
			<td>
			<ul class="list">
				<li>최종학력(졸업, 수료, 휴학, 퇴학, 재학) 증명서 1부</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;<strong>* 최종학력서류가 해외서류일 경우 한국어 번역공증서류 포함</strong></td>
		</tr>
		<tr>
			<th scope="row">해당자</th>
			<td>
			<ul class="list">
				<li>디자인 분야 실무경력 증명서 사본 1부</li>
				<li>디자인 관련 고등학교 졸업 증명서 1부</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3><span style="font-size: 12px;">※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</span><br>
<br>
선발기준</h3>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차 선발 : 서류심사평가 점수 고득점 순으로 계획인원 500% 선발<br>
	<strong>* 동점 시에는&nbsp;생년월일이 빠른 순&nbsp;선발</strong></li>
	<li>2차 선발 : 1차 선발인원 대상, 포트폴리오·실기평가, 면접 시행</li>
	<li>최종 선발 : 1차 평가점수와 무관하게, 2차 평가 고득점 순으로 선발<br>
	<strong>* 동점 시에는 생년월일이 빠른순으로 선발</strong></li>
</ul>
</div>

<div class="layout_h4">
<h4>배점기준 총괄</h4>
&nbsp;

<table class="table_col">
	<caption>선발 및 평가 배점에 대한 배점표이며 계, 1차평가, 2차평가에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_10p" rowspan="2" scope="col">계</th>
			<th class="width_60p" colspan="3" scope="col">1차 평가</th>
			<th class="width_15p" rowspan="2" scope="col">2차 평가</th>
		</tr>
		<tr>
			<th class="width_20p" scope="col">전공학과</th>
			<th class="width_20p" scope="col">실무경력</th>
			<th class="width_20p" scope="col">고교출석률</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>100</td>
			<td>15</td>
			<td>25</td>
			<td>10</td>
			<td>50</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>1차 평가</h4>

<div class="layout_h5">
<h5>전공학과</h5>

<table class="table_col">
	<caption>전공학과에 대한 배점표이며 구분, 4년제 졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 디자인관련특성화고 졸업자, 비전공에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_12p" scope="col">4년제<br>
			졸업이상</th>
			<th class="width_12p" scope="col">3년수료/<br>
			4년재학</th>
			<th class="width_12p" scope="col">2년수료/<br>
			3년재학</th>
			<th class="width_12p" scope="col">1년수료/<br>
			2년재학</th>
			<th class="width_12p" scope="col">1년재학</th>
			<th class="width_13p" scope="col">고등학교<br>
			관련학과<br>
			졸업자</th>
			<th class="width_12p" scope="col">비전공</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>15</td>
			<td>13</td>
			<td>11</td>
			<td>10</td>
			<td>9</td>
			<td rowspan="2">13</td>
			<td rowspan="2">6</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>13</td>
			<td>11</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
		</tr>
		<tr>
			<th scope="row">비 고</th>
			<td colspan="7">고등학교 관련학과&nbsp;졸업자가 대학을 진학 했을 경우, 높은 점수 1개만 인정</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>1. 직접학과 : 디자인·그래픽·만화 등 관련 학과</li>
	<li>2. 간접학과 : 언론·홍보·방송 등 관련 학과</li>
</ul>
</div>

<div class="layout_h5">
<h5>실무경력</h5>

<table class="table_col">
	<caption>실무경력에 대한 표이며 구분, 경력없음/1개월 미만/1개월~15개월까지 3개월 단위로 달라지는 배점 안내</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_12p" scope="col">15개월<br>
			이상</th>
			<th class="width_12p" scope="col">12개월~<br>
			15개월<br>
			미만</th>
			<th class="width_12p" scope="col">9개월~<br>
			12개월<br>
			미만</th>
			<th class="width_12p" scope="col">6개월~<br>
			9개월<br>
			미만</th>
			<th class="width_12p" scope="col">3개월~<br>
			6개월<br>
			미만</th>
			<th class="width_13p" scope="col">1개월~<br>
			3개월<br>
			미만</th>
			<th class="width_12p" scope="col">1개월<br>
			미만</th>
			<th class="width_12p" scope="col">경력<br>
			없음</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">25</td>
			<td style="text-align: center;">23</td>
			<td style="text-align: center;">21</td>
			<td style="text-align: center;">19</td>
			<td style="text-align: center;">17</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: center;">13</td>
			<td style="text-align: center;">11</td>
		</tr>
		<tr>
			<th scope="row">비 고</th>
			<td colspan="8" style="text-align: justify;">&nbsp; 회사명의 경력증명서 제출(범위제한 없음)<br>
			&nbsp;&nbsp; * 2차 평가 시 재직여부 확인, 허위로 밝혀질 경우 선발제외</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>고교출석률</h5>

<table class="table_col">
	<caption>고교출석률에 대한 배점 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_17p" scope="col">결석 0일</th>
			<th class="width_17p" scope="col">결석 1~2일</th>
			<th class="width_17p" scope="col">결석 3~5일</th>
			<th class="width_17p" scope="col">결석 6일 이상&nbsp;</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>2차 평가</h4>

<table class="table_col">
	<caption>2차평가에 대한 배점 표이며 구분, 면접, 직무수행능력(실기평가), 포트폴리오에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_45p" colspan="3" scope="col">면&nbsp;접</th>
			<th class="width_25p" rowspan="2" scope="col">직무수행능력<br>
			(실기평가)</th>
			<th class="width_15p" rowspan="2" scope="col">포트폴리오</th>
		</tr>
		<tr>
			<th class="width_15p" scope="col">면접태도</th>
			<th class="width_15p" scope="col">표현력/적극성</th>
			<th class="width_15p" scope="col">국가관/안보관</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>30</td>
			<td>5</td>
		</tr>
		<tr>
			<td class="text_left" colspan="6">* 직무수행능력평가 : 기획력, 포토샵·일러스트레이터 활용, 애니메이션 제작(해당자)<br>
			&nbsp; - 직무수행능력평가 항목은 평가주관부대 사정에 따라 변경될 수 있음<br>
			* 포트폴리오 : 개인 출품작, 개인 저작권을 가진 일러스트, 웹툰, 디자인 등의 작품(파일)<br>
			* 1개 항목이라도 0점 배점 시 불합격</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h3">
<h3>전공학과 목록</h3>

<table class="table_col">
	<caption>전공학과 목록 표이며 직접관련학과, 간접관련학과에 대한 정보를 제공</caption>
	<tbody>
		<tr>
			<th class="width_15p" scope="row">직접관련 학과</th>
			<td class="width_85p">광고·멀티미디어디자인과, 디지털그래픽디자인과, 웹디자인, 시각디자인, 전자출판디자인 등 ‘디자인’, ‘그래픽’, ‘만화’, ‘애니메이션’이 포함된 학과</td>
		</tr>
		<tr>
			<th class="width_15p" scope="row">간접관련 학과</th>
			<td class="width_85p">신문방송학과, 언론홍보학과 등 ‘신문’, ‘언론’, ‘홍보’, ‘방송’, ‘미디어’, '디자인'이 포함된 학과</td>
		</tr>
	</tbody>
</table>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html52="""<div id="contents">               
<div class="layout_h3">
<h3>사진콘텐츠디자이너 (341337)</h3>
<!-- <span style="font-size: 14px;">주기적으로 드론 상태 점검, 드론 및 통제장비 운용 &middot;정비 임무를 수행합니다.</span></div> --></div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본여건, 세부요건(전공학과, 기타), 지원제한에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" colspan="2" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">기본요건</th>
			<td>○ 현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원한 사람<br>
			○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">세부요건<br>
			(中1)</th>
			<th scope="row">전공학과</th>
			<td>
			<ul class="list">
				<li>사진영상과, 디지털사진과, 미디어사진과, 사진예술과 등 1년 수료 이상인 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">기타</th>
			<td>
			<ul class="list">
				<li>사진 분야 실무경력이&nbsp;15개월 이상인 사람</li>
				<li>고등학교(특성화고, 특목고 등)&nbsp;관련학과를 졸업한 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">지원제한</th>
			<td>
			<ul class="list">
				<li>범죄조회 결과 집행유예 이상의 범죄경력사실이 있는 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>
&nbsp;

<div class="layout_h3">
<h3>제출서류</h3>

<table class="table_col">
	<caption>제출서류 표이며 구분, 내용에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">필 수</th>
			<td>
			<ul class="list">
				<li>최종학력(졸업, 수료, 휴학, 퇴학, 재학) 증명서 1부</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;<strong>* 최종학력서류가 해외서류일 경우 한국어 번역공증서류 포함</strong></td>
		</tr>
		<tr>
			<th scope="row">해당자</th>
			<td>
			<ul class="list">
				<li>사진 분야 실무경력 증명서 사본 1부</li>
				<li>사진 관련 고등학교 졸업 증명서 1부</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3><span style="font-size: 12px;">※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</span><br>
<br>
선발기준</h3>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차 선발 : 서류심사평가 점수 고득점 순으로 계획인원 500% 선발<br>
	<strong>* 동점 시에는&nbsp;생년월일이 높은 순 선발</strong></li>
	<li>2차 선발 : 1차 선발인원 대상, 포트폴리오·실기평가, 면접 시행</li>
	<li>최종 선발 : 1차 평가점수와 무관하게, 2차 평가 고득점 순으로 선발<br>
	<strong>* 동점 시에는 생년월일이 빠른순으로 선발</strong></li>
</ul>
</div>

<div class="layout_h4">
<h4>배점기준 총괄</h4>
&nbsp;

<table class="table_col">
	<caption>선발 및 평가 배점에 대한 배점표이며 계, 1차 평가, 2차 평가에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_10p" rowspan="2" scope="col">계</th>
			<th class="width_60p" colspan="3" scope="col">1차 평가</th>
			<th class="width_15p" rowspan="2" scope="col">2차 평가</th>
		</tr>
		<tr>
			<th class="width_20p" scope="col">전공학과</th>
			<th class="width_20p" scope="col">실무경력</th>
			<th class="width_20p" scope="col">고교출석률</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>100</td>
			<td>15</td>
			<td>25</td>
			<td>10</td>
			<td>50</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>1차 평가</h4>

<div class="layout_h5">
<h5>전공학과</h5>

<table class="table_col">
	<caption>전공학과에 대한 배점 표이며 구분, 4년제 졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 사진관련특성화고 졸업자, 비전공에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_12p" scope="col">4년제<br>
			졸업이상</th>
			<th class="width_12p" scope="col">3년수료/<br>
			4년재학</th>
			<th class="width_12p" scope="col">2년수료/<br>
			3년재학</th>
			<th class="width_12p" scope="col">1년수료/<br>
			2년재학</th>
			<th class="width_12p" scope="col">1년재학</th>
			<th class="width_13p" scope="col">고등학교<br>
			관련학과<br>
			졸업자</th>
			<th class="width_12p" scope="col">비전공</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>15</td>
			<td>13</td>
			<td>11</td>
			<td>10</td>
			<td>9</td>
			<td rowspan="2">13</td>
			<td rowspan="2">6</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>13</td>
			<td>11</td>
			<td>9</td>
			<td>8</td>
			<td>7</td>
		</tr>
		<tr>
			<th scope="row">비 고</th>
			<td colspan="7">고등학교 관련학과 졸업자가&nbsp;대학을 진학 했을 경우, 높은 점수 1개만 인정</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>1. 직접학과 : 사진·이미지 등 관련 학과</li>
	<li>2. 간접학과 : 언론·홍보·방송 등 관련 학과</li>
</ul>
</div>

<div class="layout_h5">
<h5>실무경력</h5>

<table class="table_col">
	<caption>실무경력에 대한 표이며 구분, 경력없음/1개월 미만/1개월~15개월까지 3개월 단위로 달라지는 배점 안내</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_12p" scope="col">15개월<br>
			이상</th>
			<th class="width_12p" scope="col">12개월~<br>
			15개월<br>
			미만</th>
			<th class="width_12p" scope="col">9개월~<br>
			12개월<br>
			미만</th>
			<th class="width_12p" scope="col">6개월~<br>
			9개월<br>
			미만</th>
			<th class="width_12p" scope="col">3개월~<br>
			6개월<br>
			미만</th>
			<th class="width_13p" scope="col">1개월~<br>
			3개월<br>
			미만</th>
			<th class="width_12p" scope="col">1개월<br>
			미만</th>
			<th class="width_12p" scope="col">경력<br>
			없음</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td style="text-align: center;">25</td>
			<td style="text-align: center;">23</td>
			<td style="text-align: center;">21</td>
			<td style="text-align: center;">19</td>
			<td style="text-align: center;">17</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: center;">13</td>
			<td style="text-align: center;">11</td>
		</tr>
		<tr>
			<th scope="row">비 고</th>
			<td colspan="8" style="text-align: justify;">&nbsp; 회사명의 경력증명서 제출(범위제한 없음)<br>
			&nbsp;&nbsp; * 2차 평가 시 재직여부 확인, 허위로 밝혀질 경우 선발제외</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>고교출석률</h5>

<table class="table_col">
	<caption>고교출석률에 대한 배점 표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_17p" scope="col">결석 0일</th>
			<th class="width_17p" scope="col">결석 1~2일</th>
			<th class="width_17p" scope="col">결석 3~5일</th>
			<th class="width_17p" scope="col">결석 6일 이상&nbsp;</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align: left;">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>2차 평가</h4>

<table class="table_col">
	<caption>2차 평가에 대한 배점표이며 계, 면접, 직무수행능력(실기평가), 포트폴리오에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_45p" colspan="3" scope="col">면&nbsp;접</th>
			<th class="width_25p" rowspan="2" scope="col">직무수행능력<br>
			(실기평가)</th>
			<th class="width_15p" rowspan="2" scope="col">포트폴리오</th>
		</tr>
		<tr>
			<th class="width_15p" scope="col">면접태도</th>
			<th class="width_15p" scope="col">표현력/적극성</th>
			<th class="width_15p" scope="col">국가관/안보관</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>30</td>
			<td>5</td>
		</tr>
		<tr>
			<td class="text_left" colspan="6">* 직무수행능력평가 : 사진 촬영 및 편집(포토숍 활용)<br>
			&nbsp; - 직무수행능력평가 항목은 평가주관부대 사정에 따라 변경될 수 있음<br>
			* 포트폴리오 : 개인 출품작, 개인 저작권을 가진 사진집(인쇄물 또는 파일)<br>
			* 1개 항목이라도 0점 배점 시 불합격</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h3">
<h3>전공학과 목록</h3>

<table class="table_col">
	<caption>전공학과 목록 표이며 직접관련학과, 간접관련학과에 대한 정보를 제공</caption>
	<tbody>
		<tr>
			<th class="width_15p" scope="row">직접관련 학과</th>
			<td class="width_85p">디지털사진영상과, 디지털이미지학과, 사진예술학과, 미디어사진과, 광고사진과 등 ‘사진’, ‘이미지’가 포함된 학과</td>
		</tr>
		<tr>
			<th class="width_15p" scope="row">간접관련 학과</th>
			<td class="width_85p">신문방송학과, 언론홍보학과 등 ‘신문’, ‘언론’, ‘홍보’, ‘방송’, ‘미디어’, '디자인'이 포함된 학과</td>
		</tr>
	</tbody>
</table>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html53="""<div id="contents">	                    
<div class="layout_h3">
<h3>기동헬기운용병 (182339)</h3>
<!-- <span style="font-size: 14px;">주기적으로 드론 상태 점검, 드론 및 통제장비 운용 &middot;정비 임무를 수행합니다.</span></div> --></div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 세부요건(전공학과, 기타), 지원제한에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" colspan="2" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">세부요건<br>
			(中1)</th>
			<th scope="row">전공학과</th>
			<td>
			<ul class="list">
				<li>헬기(회전익)정비학과, 항공정비학과, 항공기계과, 항공전자과, 항공운항과 1년 재학 이상인 사람(우주항공공학 지원 불가)&nbsp;</li>
				<li>고졸인 경우 해당학과를 졸업한 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">기타</th>
			<td>
			<ul class="list">
				<li>항공정비사, 항공기술사, 항공기사, 항공산업기사 자격증을 취득한 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">지원제한</th>
			<td>
			<ul class="list">
				<li>수지결손, 수지강직, 시각장애, 수전증, 청각장애, 색각장애, 운동장애, 언어장애, 디스크/관절 이상, 정신건강의학과 질환이 있는 사람</li>
				<li>범죄조회 결과&nbsp;집행유예 이상의 범죄경력사실이 있는 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능&nbsp;&nbsp;</li>
</ul>
</div>

<div class="layout_h3">
<h3>제출서류</h3>

<table class="table_col">
	<caption>제출서류에 대한 표이며 구분, 내용에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">필 수</th>
			<td>
			<ul class="list">
				<li>최종학력(졸업, 수료, 휴학, 퇴학, 재학) 증명서 1부</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;<strong>* 최종학력 증빙서류가 해외서류일 경우 한국어 번역공증서 포함</strong></td>
		</tr>
		<tr>
			<th scope="row">해당자</th>
			<td>
			<ul class="list">
				<li>자격증 사본 1부</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;<strong>* 자격증 증빙서류가 해외서류일 경우 한국어 번역공증서 포함</strong>

			<ul class="list">
				<li>항공정비 관련 군 특성화고 졸업 증명서 1부.</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3><span style="font-size: 12px;">※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</span><br>
<br>
선발기준</h3>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차 선발 : 서류심사평가 점수 고득점 순으로 계획인원 200% 선발(동점 시 생년월일이 빠른 순)</li>
	<li>최종 선발 : 1차 평가와 2차 평가 합산하여 고득점 순 선발(동점 시 면접/실기점수가 높은 순, 생년월일이 빠른 순)</li>
</ul>
</div>

<div class="layout_h4">
<h4>배점기준 총괄</h4>

<table class="table_col">
	<caption>배점기준 대한 배점표이며 구분, 1차평가(서류심사), 2차평가(면접/실무평가)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_10p" rowspan="2" scope="col">계</th>
			<th class="width_50p" colspan="2" scope="col">1차 평가(서류심사)</th>
			<th class="width_25p" rowspan="2" scope="col">2차 평가<br>
			(면접/실무평가)</th>
		</tr>
		<tr>
			<th class="width_25p" scope="col">전공학과</th>
			<th class="width_25p" scope="col">자격증</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>100</td>
			<td>20</td>
			<td>25</td>
			<td>55</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>1차 평가</h4>

<div class="layout_h5">
<h5>전공학과</h5>

<table class="table_col">
	<caption>전공학과에 대한 배점 표이며 구분, 4년제 졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학, 고졸이하/미전공에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_14p" scope="col">4년제<br>
			졸업이상</th>
			<th class="width_14p" scope="col">3년수료/<br>
			4년재학</th>
			<th class="width_14p" scope="col">2년수료/<br>
			3년재학</th>
			<th class="width_14p" scope="col">1년수료/<br>
			2년재학</th>
			<th class="width_14p" scope="col">1년재학</th>
			<th class="width_15p" scope="col">고졸이하/<br>
			미전공</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">직접학과</th>
			<td>20</td>
			<td>18</td>
			<td>16</td>
			<td>14</td>
			<td>12</td>
			<td rowspan="2">8</td>
		</tr>
		<tr>
			<th scope="row">간접학과</th>
			<td>18</td>
			<td>16</td>
			<td>14</td>
			<td>12</td>
			<td>10</td>
		</tr>
	</tbody>
</table>

<ul class="list">
	<li>1. 직접학과 : 헬기(회전익)정비학과, 항공정비학과, 항공기계과, 항공전자과</li>
	<li>2. 간접학과 : 항공운항과<br>
	<strong>* 항공정비 관련 군 특성화고 졸업인원은 8점을 가산하되, 최대 20점 초과 불가</strong></li>
</ul>
</div>

<div class="layout_h5">
<h5>자격증</h5>

<table class="table_col">
	<caption>자격증에 대한 배점표이며 구분, 국내 공인자격증에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_85p" colspan="2" scope="col">국내 공인자격증</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th rowspan="3" scope="col">자격증별<br>
			배 점</th>
			<td class="width_75p">
			<ul class="list">
				<li>항공기술사(한국산업인력관리공단)</li>
			</ul>
			</td>
			<td class="width_10p">25</td>
		</tr>
		<tr>
			<td class="width_75p">
			<ul class="list">
				<li>항공기사(한국산업인력관리공단)</li>
				<li>항공정비사(교통안전관리공단)</li>
			</ul>
			&nbsp;<strong>* 미국 및 유럽 민간항공청(FAA, EASA)에서 발행한 동급 자격(면허)증</strong></td>
			<td class="width_10p">23</td>
		</tr>
		<tr>
			<td>
			<ul class="list">
				<li>항공산업기사(한국산업인력관리공단)</li>
			</ul>
			</td>
			<td>20</td>
		</tr>
		<tr>
			<th rowspan="2" scope="col">미취득</th>
			<td>
			<ul class="list">
				<li>관련학과 재학/졸업</li>
			</ul>
			</td>
			<td>10</td>
		</tr>
		<tr>
			<td>
			<ul class="list">
				<li>비관련학과 재학/졸업</li>
			</ul>
			</td>
			<td>0</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>2차 평가</h4>

<table class="table_col">
	<caption>2차 평가에 대한 배점표이며 구분, 계, 면접, 실무평가(정비능력)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_15p" scope="col">계</th>
			<th class="width_30p" scope="col">면&nbsp;접</th>
			<th class="width_30p" scope="col">실무평가(정비능력)</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>55</td>
			<td>20</td>
			<td>35</td>
		</tr>
		<tr>
			<td class="text_left" colspan="4">* 2차평가 결과가 38.5점 이하인 사람은&nbsp;선발제외 처리</td>
		</tr>
	</tbody>
</table>
</div>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html54="""<div id="contents">                          
<!-- 요약 문구 start -->

<div class="board_box">
<ul class="list noPbottom">
	<li>지원 자격 :&nbsp;신체등급 1부터 3급까지 현역병입영대상자로 병역처분된 사람으로 관련 모집분야 석사 재학(휴학) 이상자(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</li>
	<li>지원제한 : 범죄조회 결과 집행유예 이상의 범죄경력사실이 있는&nbsp;사람/수사 또는 재판중에 있는 사람/처분미상으로 통보된 사람, '대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
	<li>모집 분야 : 첨단센서연구병 등 23개 분야</li>
</ul>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* 현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * 각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한(다만, 선발취소되거나&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능)
<p><br>
※ 모집분야 별 세부 내용은 아래 링크된 파일을 참조하시기 바라며, 군 소요계획&nbsp;따라 다소 변경될 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp;☞ 분야별 세부 접수(전형)일정&nbsp;및&nbsp;내용은 모집하는 월의 세부 모집계획을 확인하시기 바랍니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (면접평가 장소도 사정에 따라 변경될 수 있으니, 모집하는 월의 세부 모집계획을 확인하시기 바랍니다.)&nbsp;</p>
</div>
<!-- 요약 문구 end -->

<div class="layout_h4">
<h4>군사과학기술병 안내 자료<span class="button down white2 ml10px"><a href="/cmfileDown.do?gtfile_no=195" target="_self">다운로드</a><a href="/cmfileView.do?gtfile_no=195" target="_blank">미리보기</a></span></h4>
&nbsp;&nbsp; 군사과학기술병 소개 영상(<a href="https://youtu.be/aioFKTBYmkc"><span style="color: rgb(0, 102, 204);">https://youtu.be/aioFKTBYmkc</span></a>)</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html55="""<div id="contents">	                
<div class="layout_h3">
<h3>과학수사병 (321254)</h3>
</div>

<div class="layout_h3">
<h3>선발 개요</h3>

<div class="layout_h4">
<h4>임무</h4>

<ul class="list">
	<li>과학수사시스템 등 각종 시스템 운용 지원</li>
	<li>발생 사건·사고 수사속보 작성 보조</li>
	<li>육군 인터넷, 인트라넷 망 침해범죄 수사 보조</li>
	<li>사건 사고 현장감식 등 지원</li>
	<li>육군 사이버순찰대 운용 현황 종합 및 사이버 모니터링</li>
</ul>
</div>

<h3 class="layout_h4">선발방법 : 1차 서류전형 / 2차 면접</h3>

<div class="layout_h4">
<h4>2차 평가 장소 : 인재선발지원센터(충남 계룡시 신도안면 정장리 370-1)<br>
*네비게이션 : 인재선발센터</h4>
</div>
</div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격에 대한 표이며 구분, 연력, 기본요건, 세부요건(전공학과, 신체조건), 지원제한에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" colspan="2" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 3급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 3급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">세부요건</th>
			<th scope="row">전공학과</th>
			<td>경찰계열, 이공계열&nbsp;관련 전공학과 1학년 재학 이상<br>
			* 경찰계열 : 경찰행정, 과학수사, 국방경찰학 등, 이공계열 : 전산학, 컴퓨터공학, 정보통신공학 등</td>
		</tr>
		<tr>
			<th scope="row">신체조건</th>
			<td>신장 161cm 이상인 사람</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">지원제한</th>
			<td>
			<ul class="list">
				<li>범죄조회 결과 징역 또는 금고의 형의 실형(집행유예포함)을 선고 받은 자, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>각 군 현역병에 지원 중이거나 지원하여 합격한 사람(선발취소 되거나, 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원가능)</li>
				<li>운동장애(수지결손, 수지강직 포함), 청각/언어장애, 수전증, 색각장애가 있는 사람</li>
				<li>민소매/짧은 반바지 착용시 외관상 보이는 곳에 문신이 있는 사람&nbsp;&nbsp;</li>
				<li>정신건강의학과 질환이 있는 사람(병역판정검사&nbsp;결과 정신과 사유 3급 판정자)&nbsp;</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>
</div>

<div class="layout_h3">
<h3>제출서류</h3>

<table class="table_col">
	<caption>제출서류에 대한 표이며 구분, 내용에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">필 수</th>
			<td>
			<ul class="list">
				<li>최종학력(졸업, 수료, 휴학, 퇴학, 재학) 증명서 1부<br>
				<strong>&nbsp;* 최종학력서류가 해외서류일 경우 한국어 번역공증서류 포함</strong></li>
				<li>고교생활기록부 1부.</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">해당자</th>
			<td>자격증 사본 1부, 어학성적표 사본 1부</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3><span style="font-size: 12px;">※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</span><br>
<br>
선발기준</h3>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차선발 : 서류심사평가 점수 고득점 순으로 계획인원 300% 선발<br>
	&nbsp;＊동점시 : 전공점수가 높은 순, 고교출석률이 높은 순, 생년월일이 빠른 순 선발</li>
	<li>1차 평가와 2차 평가를 합산하여 고득점 순 선발<br>
	&nbsp;＊동점시 : 면접점수가 높은 순, 전공점수가 높은 순, 고교출석률이 높은 순, 생년월일이 빠른 순 선발</li>
</ul>
</div>

<div class="layout_h4">
<h4>배점기준 총괄</h4>
&nbsp;

<table class="table_col">
	<caption>배점기준에 대한 배점 표이며 총점, 계, 서류심사(1차 평가), 2차 평가(면접)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">총&nbsp;점</th>
			<th class="width_10p" rowspan="2" scope="col">계</th>
			<th class="width_60p" colspan="4" scope="col">서류심사 (1차 평가)</th>
			<th class="width_15p" rowspan="2" scope="col">2차 평가<br>
			(면접)</th>
		</tr>
		<tr>
			<th class="width_15p" scope="col">전공학과</th>
			<th class="width_15p" scope="col">고교출석률</th>
			<th class="width_15p" scope="col">자격증</th>
			<th class="width_15p" scope="col">어학능력</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>100</td>
			<td>30</td>
			<td>10</td>
			<td>5</td>
			<td>5</td>
			<td>50</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>1차 평가(서류심사)</h4>

<div class="layout_h5">
<h5>전공학과(30점)</h5>

<table class="table_col">
	<caption>전공학과에 대한 배점 표이며, 구분, 4년제 졸업이상, 3년수료/4년재학, 2년수료/3년재학, 1년수료/2년재학, 1년재학에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구 분</th>
			<th class="width_17p" scope="col">4년제 졸업<br>
			이상</th>
			<th class="width_17p" scope="col">3년 수료<br>
			4년 재학</th>
			<th class="width_17p" scope="col">2년 수료<br>
			3년 재학</th>
			<th class="width_17p" scope="col">1년 수료<br>
			2년 재학</th>
			<th class="width_17p" scope="col">1년 재학</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>30</td>
			<td>27</td>
			<td>24</td>
			<td>21</td>
			<td>18</td>
		</tr>
	</tbody>
</table>
</div>
&nbsp; ※ 관련(인정)학과<br>
&nbsp;&nbsp;&nbsp;1. 경찰계열<br>
&nbsp;&nbsp;&nbsp; 경찰대학(법학과, 행정학과) 경찰법학과(부), 경찰행정학과(부), 경찰법행정학과(부), 경찰법학과(부),<br>
&nbsp;&nbsp;&nbsp; 사이버경찰학, 과학수사학과(부), 경찰법무전공, 경찰법행정, 경찰사이버보안과, 사이버경찰학과(부),<br>
&nbsp;&nbsp; &nbsp;경찰공무원과, 법무경찰행정과, 법무행정경찰학과, 경찰행정경영학부, 공무원경찰과, 법경찰학과(부),<br>
&nbsp;&nbsp;&nbsp; 사이버수사경찰학과(부), 사이버경찰보안, 법행정경찰학부, 경찰학과(부), 법경찰학과,<br>
&nbsp;&nbsp;&nbsp; 국방경찰행정학과(부), 행정경찰학과(부), 경찰부사관과 등<br>
&nbsp;&nbsp;&nbsp; ✽ 경찰학 관련전공 중 비서·의전·복지·기관 등은 제외<br>
&nbsp; <span style="color: rgb(255, 0, 0);">&nbsp;2. 이공계열('22.10월 추가 적용)<br>
&nbsp;&nbsp;&nbsp; 전산학ㆍ컴퓨터공학과(부), 빅데이터학과(부), IT소프트웨어학과(부), 컴퓨터학과(부), 인터넷정보학과(부),<br>
&nbsp;&nbsp;&nbsp; 전자공학과(부), 전자정보통신공학과(부), 사이버보안과(부), 포렌식학과(부), 사이버해킹보안과(부),<br>
&nbsp;&nbsp;&nbsp; 화학공학계열과(부), 생명공학계열과(부), 유전자분석계열과(부)&nbsp;</span>

<div data-hjsonver="1.0" data-jsonlen="9717"><span style="color: rgb(255, 0, 0);">&nbsp;&nbsp;&nbsp;&nbsp;</span></div>

<div class="layout_h5">
<h5>고교출석률(10점)</h5>

<table class="table_col">
	<caption>고교출석률에 대한 배점표이며 구분, 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_21p" scope="col">결석 0일</th>
			<th class="width_21p" scope="col">결석 1~2일</th>
			<th class="width_21p" scope="col">결석 3~5일</th>
			<th class="width_22p" scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배&nbsp;점</th>
			<td>10</td>
			<td>9</td>
			<td>7</td>
			<td>4</td>
		</tr>
		<tr>
			<td class="text_left" colspan="5">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>자격증(5점)</h5>

<table class="table_col">
	<caption>자격증에 대한 배점표이며 구분, 기능사 이상, 일반자격, 기본에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구&nbsp;분</th>
			<th class="width_20p" rowspan="2" scope="col">기능사 이상</th>
			<th class="width_50p" colspan="2" scope="col">일반자격</th>
			<th class="width_15p" rowspan="2" scope="col">기본</th>
		</tr>
		<tr>
			<th class="width_25p" scope="col">1급</th>
			<th class="width_25p" scope="col">2급</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배&nbsp;점</th>
			<td>5</td>
			<td>4</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<th scope="col">자격증</th>
			<td>정보처리<br>
			정보기기운용</td>
			<td>컴퓨터활용능력<br>
			인터넷정보관리사<br>
			MOS(Expert)</td>
			<td>컴퓨터활용능력<br>
			인터넷정보관리사<br>
			MOS(Core)</td>
			<td></td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>어학(영어) 능력(5점)</h5>

<table class="table_col">
	<caption>어학능력에 대한 배점 표이며 구분,&nbsp;TOEIC 790점 이상,&nbsp;TEPS 390점 이상,&nbsp;TOEFL(IBT) 80점 이상, 기본에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_25p" scope="col">TOEIC 790점 이상</th>
			<th class="width_25p" scope="col">TEPS 390점 이상</th>
			<th class="width_25p" scope="col">TOEFL(IBT) 80점 이상</th>
			<th class="width_10p" scope="col">기본</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배&nbsp;점</th>
			<td colspan="3">5</td>
			<td>3</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>2차 평가(면접)</h4>

<table class="table_col">
	<caption>2차 평가(면접)에 대한 배점표이며 구분, 계, 면접 태도, 표현/발표력, 국가관, 대인관계역량, 직무능력(전공지식)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_10p" scope="col">계</th>
			<th class="width_15p" scope="col">면접 태도</th>
			<th class="width_15p" scope="col">표현/<br>
			발표력</th>
			<th class="width_15p" scope="col">국가관</th>
			<th class="width_15p" scope="col">대인관계<br>
			역량</th>
			<th class="width_15p" scope="col">직무능력<br>
			(전공지식)</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>50</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>30</td>
		</tr>
		<tr>
			<td class="text_left" colspan="7">* 2차 평가(면접) 총점 60%(30점) 미만 평가 시&nbsp;선발제외 처리</td>
		</tr>
	</tbody>
</table>
</div>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html56="""<div id="contents">                  
<div class="layout_h3">
<h3>JSA경비병 (111000)</h3>
</div>

<div class="layout_h3">
<h3>선발 개요</h3>

<div class="layout_h4">
<h4>임무</h4>

<ul class="list">
	<li>판문점 공동경비구역(JSA) 내 출입인원 경호 및 DMZ 작전</li>
	<li>공동경비구역 내 남북회담 및 각종 국가사업 시 경호</li>
	<li>중립국감독위원회(NNSC) 및 대성동 주민 경호</li>
</ul>
</div>

<div class="layout_h4">
<h3>선발방법 : 1차 서류전형 / 2차 면접</h3>
</div>

<div class="layout_h4">
<h4>2차 평가 장소 : 대전충남지방병무청</h4>
</div>
</div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격에 대한 표이며 구분, 연력, 기본요건, 신체조건, 지원제한에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세 이상 28세 이하(2023년 기준 : 1995.1.1 ~ 2005.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○ 다음 중 어느하나에 해당되는 사람<br>
			&nbsp; ▶ 신체등급 1급부터 2급까지 현역병입영대상자로 병역처분된&nbsp;사람<br>
			<span style="font-size: 13px;">&nbsp; ▶ </span>병역판정검사<span style="font-size: 13px;">를 받지 아니한 사람(18세자 포함)은 현역병지원 신체검사 결과 </span>신체등급 1급부터 2급까지<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th scope="row">신체조건</th>
			<td>
			<ul class="list">
				<li>신장 174cm 이상, 체중 65㎏ 이상,</li>
				<li>교정시력 1.0 이상인 사람</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한</th>
			<td>
			<ul class="list">
				<li>범죄경력 조회 결과 기소유예 이상의 형을 선고 받은 사람</li>
				<li>수사 또는 재판 중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>각 군 현역병에 지원 중이거나 지원하여 합격한 사람(선발취소 되거나, 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원가능)</li>
				<li>디스크/관절 이상, 색각/언어/청력 장애가 있는 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp;선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>
</div>

<div class="layout_h3">
<h3>제출서류</h3>

<table class="table_col">
	<caption>제출서류에 대한 표이며 구분, 내용에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" scope="col">구&nbsp;분</th>
			<th class="width_80p" scope="col">내&nbsp;용</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">필 수</th>
			<td>고교생활기록부 1부.</td>
		</tr>
		<tr>
			<th scope="row">해당자</th>
			<td>무도단증 사본 1부, 자격증 사본 1부.</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3><span style="font-size: 12px;">※ 지원서 작성 시 첨부하지 않은 구비서류는 접수마감일 다음날까지 응시지역 지방병무(지)청 (모병담당)에 반드시 제출하여야 함</span><br>
<br>
선발기준</h3>

<div class="layout_h4">
<h4>선발방식</h4>

<ul class="list">
	<li>1차선발 : 서류심사평가 점수 고득점 순으로 계획인원 200% 선발<br>
	&nbsp;＊동점시 : 고교출석률이 높은 순, 생년월일이 빠른 순 선발</li>
	<li>최종선발 : 1차 평가와 2차 평가를 합산하여 고득점 순 선발<br>
	&nbsp;＊동점시 : 2차 전형점수가 높은 순, 고교출석률이 높은 순, 생년월일이 빠른 순 선발</li>
</ul>
</div>

<div class="layout_h4">
<h4>배점기준 총괄</h4>

<table class="table_col">
	<caption>배점기준에 대한 배점표이며 총점, 계, 1차 평가(서류심사), 2차 평가에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">총&nbsp;점</th>
			<th class="width_10p" rowspan="2" scope="col">계</th>
			<th class="width_50p" colspan="3" scope="col">1차 평가(서류심사)</th>
			<th class="width_25p" colspan="2" scope="col">2차 평가</th>
		</tr>
		<tr>
			<th class="width_17p" scope="col">무도단증</th>
			<th class="width_16p" scope="col">자격증</th>
			<th class="width_17p" scope="col">고교출석률</th>
			<th class="width_12p" scope="col">면접</th>
			<th class="width_13p" scope="col">체력평가</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>100</td>
			<td>10</td>
			<td>5</td>
			<td>15</td>
			<td>50</td>
			<td>20</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>1차 평가(서류심사)</h4>

<div class="layout_h5">
<h5>무도단증(10점)</h5>

<table class="table_col">
	<caption>무도단증에 대한 배점 표이며, 구분, 태권도,유도,합기도 단증보유자(기타 무도단증은 불인정)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" rowspan="2" scope="col">구 분</th>
			<th class="width_85p" colspan="6" scope="col">태권도, 유도, 합기도 단증 보유자(기타 무도단증은 불인정)</th>
		</tr>
		<tr>
			<th class="width_15p" scope="col">5단 이상</th>
			<th class="width_14p" scope="col">4단</th>
			<th class="width_14p" scope="col">3단</th>
			<th class="width_14p" scope="col">2단</th>
			<th class="width_14p" scope="col">1단</th>
			<th class="width_14p" scope="col">없음</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배점</th>
			<td>10</td>
			<td>8</td>
			<td>6</td>
			<td>4</td>
			<td>2</td>
			<td>0</td>
		</tr>
		<tr>
			<td class="text_left" colspan="7">* 단수 합계 산정 : 태권도 2단 + 유도 1단 ⇒ 6점 부여(최대 10점)</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>자격증(5점)</h5>

<table class="table_col">
	<caption>자격증에 대한 배점표이며 구분,&nbsp;경호지도사, 경비지도사, 응급구조사, 인명구조요원, 기본에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_70p" scope="col">경호지도사, 경비지도사, 응급구조사, 인명구조요원</th>
			<th class="width_15p" scope="col">기본</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배&nbsp;점</th>
			<td>5</td>
			<td>2</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>고교출석률(10점)</h5>

<table class="table_col">
	<caption>고교출석률에 대한 배점 표이며 결석 0일, 결석 1~2일, 결석 3~5일, 결석 6일 이상에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_21p" scope="col">결석 0일</th>
			<th class="width_21p" scope="col">결석 1~2일</th>
			<th class="width_21p" scope="col">결석 3~5일</th>
			<th class="width_22p" scope="col">결석 6일 이상</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="col">배&nbsp;점</th>
			<td>15</td>
			<td>13</td>
			<td>10</td>
			<td>8</td>
		</tr>
		<tr>
			<td class="text_left" colspan="5">
			<div style="text-align: left;">&nbsp;* 검정고시 합격자/ 외국의 고교졸업자/초등학교 이하 학력자&nbsp;:&nbsp;지원자의 평균점수 적용<br>
			&nbsp;* 지각/조퇴 2회는 결석 1일로 처리<br>
			&nbsp;* 결과(교과시간에 출석하지 않은 경우) 2회는 지각(조퇴) 1회로 처리</div>

			<div style="text-align: left;">&nbsp;* 질병에 의한 결석, 결과, 지각은 적용하지 않음</div>
			</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>2차 평가(면접/체력)</h4>

<div class="layout_h5">
<h5>면접(50점)</h5>

<table class="table_col">
	<caption>면접에 대한 배점 표이며 구분, 계, 지원동기/품성, 표현/발표력, 대인관계역량, 면접태도에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_15p" scope="col">구&nbsp;분</th>
			<th class="width_10p" scope="col">계</th>
			<th class="width_18p" scope="col">지원동기 /<br>
			품성</th>
			<th class="width_19p" scope="col">표현 / 발표력</th>
			<th class="width_19p" scope="col">대인관계역량</th>
			<th class="width_19p" scope="col">면접 태도</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">배 점</th>
			<td>50</td>
			<td>15</td>
			<td>15</td>
			<td>10</td>
			<td>10</td>
		</tr>
		<tr>
			<td class="text_left" colspan="6">＊2차 평가(면접) 총점 60%(30점) 미만 평가시 선발제외&nbsp;처리</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>체력평가(20점)</h5>

<table class="table_col">
	<caption>체력에 대한 배점 표이며 종목/등급, 팔굽혀펴기(2분), 윗몸일으키기(2분)에 대한 정보를 제공</caption>
	<thead>
		<tr>
			<th class="width_20p" rowspan="2" scope="col">종목 / 등급</th>
			<th class="width_16p" scope="col">특급</th>
			<th class="width_16p" scope="col">1급</th>
			<th class="width_16p" scope="col">2급</th>
			<th class="width_16p" scope="col">3급</th>
			<th class="width_16p" rowspan="2" scope="col">선발제외</th>
		</tr>
		<tr>
			<th scope="col">10점</th>
			<th scope="col">9점</th>
			<th scope="col">8점</th>
			<th scope="col">7점</th>
		</tr>
	</thead>
	<tbody class="text_center">
		<tr>
			<th scope="row">팔굽혀펴기(2분)</th>
			<td>72개 이상</td>
			<td>64~71개</td>
			<td>56~63개</td>
			<td>48~55개</td>
			<td>47개 이하</td>
		</tr>
		<tr>
			<th scope="row">윗몸일으키기(2분)</th>
			<td>86개 이상</td>
			<td>78~85개</td>
			<td>70~77개</td>
			<td>62~69개</td>
			<td>62개 이하</td>
		</tr>
		<tr>
			<td class="text_left" colspan="6">＊팔굽혀펴기(10점), 윗몸일으키기(10점)의 합산점수 적용(총 20점)<br>
			＊2종목 중 1개 종목&nbsp;3급(7점)&nbsp;미만이어도&nbsp;선발제외 처리</td>
		</tr>
	</tbody>
</table>
</div>
</div>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html57="""<div id="contents">                    
<div class="layout_h3">
<h3>국군체육특기병&nbsp;(E00001)</h3>
<span style="font-size: 14px;">국군체육부대령에 따른 국군대표운동선수단 소속으로 각종 대회 참가 등 국군대표선수 임무를 수행합니다.</span></div>

<div class="layout_h3">
<h3>지원자격</h3>

<table class="table_col">
	<caption>지원자격 표이며 연령, 기본요건, 자격요건, 지원제한 대상에 대한 정보를 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_80p">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 19세 이상 27세 이하(2023년 기준 : 1994.1.1 ~ 2004.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">기본요건</th>
			<td>○&nbsp;신체등급 1급부터 4급까지 현역병입영대상자로 병역처분된&nbsp;사람</td>
		</tr>
		<tr>
			<th scope="row">자격요건</th>
			<td>
			<ul class="list">
				<li>대한체육회 회원종목단체 또는 프로경기단체에 등록된 선수</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">지원제한 대상</th>
			<td>
			<ul class="list">
				<li>범죄조회 결과 징역 또는 금고의 형의 실형(집행유예 포함)을 선고받은 사람, 수사 또는 재판중에 있는 사람, 처분미상으로 통보된 사람</li>
				<li>'대체역의 편입 및 복무 등에 관한 법률'에 따라 대체역 편입원을 제출한 사람</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<ul>
	<li>*&nbsp;현역병(징집병) 입영기일이 결정된 사람은 그 입영기일 30일전까지 지원 가능</li>
	<li>*&nbsp;각 군 현역병 모집에 지원중이거나 지원하여&nbsp; 선발된 사람은 지원을 제한. 다만, 선발취소 되거나 지원입영 후 귀가한 사람 등 지원에 의한 입영의무가 해소된 사람은 지원 가능</li>
</ul>

<div class="layout_h3">
<h3>구비서류</h3>

<div class="layout_h4">
<h4>제출할 서류</h4>

<ul class="list">
	<li>선수등록확인서(접수일 기준 최근 10일 이내 발행본)<br>
	&nbsp;* 단, 선수등록 기간 중이거나 등록 기간이 도래하지 않아 접수년도 자료를 제출할 수 없는 경우 전년도 자료 제출 가능</li>
	<li>경기실적증명서(해당 종목 협회 또는 연맹 발행)<br>
	&nbsp;&nbsp;&nbsp;※ 종목별 제출기간
	<table class="table_col">
		<tbody>
			<tr>
				<td style="text-align: center;">1년 이내</td>
				<td style="text-align: center;">2년 이내</td>
				<td style="text-align: center;">3년 이내</td>
			</tr>
			<tr>
				<td style="text-align: center;">배구</td>
				<td style="text-align: center;">근대5종, 사격, 사이클, 수영, 역도,<br>
				육상, 축구,농구, 럭비, 야구, 핸드볼</td>
				<td style="text-align: center;">레슬링, 바이애슬론, 복싱, 양궁, 유도,<br>
				하키, 체조, 태권도, 펜싱, 테니스,<br>
				배드민턴, 야구</td>
			</tr>
		</tbody>
	</table>
	</li>
	<li>대표경력확인서(전ㆍ현직 국가대표, 상비군, 대학ㆍ청소년 대표)&nbsp;&nbsp;&nbsp; *&nbsp;외국 경력은 미인정&nbsp;<br>
	&nbsp;&nbsp;&nbsp;※&nbsp;종목별 제출기간
	<table class="table_col">
		<tbody>
			<tr>
				<td style="text-align: center;">1년 이내</td>
				<td style="text-align: center;">2년 이내</td>
				<td style="text-align: center;">3년 이내</td>
				<td style="text-align: center;">3년 초과</td>
			</tr>
			<tr>
				<td style="text-align: center;">배구</td>
				<td style="text-align: center;">근대5종, 사격, 사이클,<br>
				수영, 역도, 육상, 축구,<br>
				농구, 핸드볼</td>
				<td style="text-align: center;">레슬링, 바이애슬론, 복싱, 양궁,<br>
				유도, 체조, 태권도, 펜싱, 테니스,<br>
				탁구, 하키, 럭비</td>
				<td style="text-align: center;">축구(U-22)<br>
				배드민턴<br>
				야구(5년)</td>
			</tr>
		</tbody>
	</table>
	* 출전기록 제출 필요 종목 : 축구(U-22 포함), 농구, 배구, 하키, 테니스, 수영, 유도, 레슬링, 사이클, 양궁, 펜싱,<br>
	역도, 복싱, 체조, 핸드볼, 럭비, 근대5종, 바이애슬론<br>
	* 대회참가확인서(증)는 미인정(단, 축구(U-22)는 인정</li>
	<li>고교생활기록부(생활기록부 출결사항 공동이용 동의자는 제출 생략)</li>
	<li>종목별 추가서류(국군체육부대 체력평가 시 직접 제출
	<table class="table_col">
		<tbody>
			<tr>
				<td style="text-align: center;">종목</td>
				<td style="text-align: center;">제출서류</td>
				<td style="text-align: center;">세부내용</td>
			</tr>
			<tr>
				<td style="text-align: center;">농구</td>
				<td style="text-align: center;">경기성적증명서</td>
				<td>최근 2년간 경기성적 제출<br>
				&nbsp;* 아마추어 : 개인기록증명서<br>
				&nbsp;* 프로 : 선수별 기록-시즌별 기록</td>
			</tr>
			<tr>
				<td style="text-align: center;">배드민턴</td>
				<td>
				<div style="text-align: center;">경기출전기록지,</div>

				<div style="text-align: center;">대회참가확인서</div>
				</td>
				<td>최근 3년간 경기실적증명서상 없는<br>
				개인/단체 경기 출전에 대한 증명서</td>
			</tr>
			<tr>
				<td style="text-align: center;">탁구</td>
				<td style="text-align: center;">경기출전기록지</td>
				<td>최근 3년간 단체경기 실적에 대한<br>
				경기실적 기록지 추가 제출</td>
			</tr>
			<tr>
				<td style="text-align: center;">테니스</td>
				<td style="text-align: center;">개인랭킹 확인서</td>
				<td>접수일 기준 7일 이내 발행<br>
				&nbsp;* 대한테니스협회(<a href="https://kortennis.co.kr/"><font color="#0066cc">Https://kortennis.co.kr</font></a>)<br>
				→선수→랭킹→남 단식→해당연도 랭킹 전기록 출력<br>
				→본인 이름에 표시</td>
			</tr>
			<tr>
				<td rowspan="2" style="text-align: center;">야구</td>
				<td style="text-align: center;">개인기록증명서</td>
				<td>최근 2년간 기록(KBO, 퓨처스)<br>
				&nbsp;* 투수 : 이닝, 방어율 포함<br>
				&nbsp;* 타자 : 타석, 타율, 홈런기록 포함<br>
				&nbsp;* KBO누리집(<a href="https://koreabaseball.co.kr">https://koreabaseball.co.kr</a>)<br>
				→선수→선수조회→팀/포지션 선택 후 본인이름<br>
				→KBO정규시즌(퓨처스리그) 확인(기록보기)<br>
				→해당연도 통산기록 출력</td>
			</tr>
			<tr>
				<td style="text-align: center;">1군 등록일수 확인서</td>
				<td>최근 2년간 기록<br>
				&nbsp;* KBO누리집(<a href="https://koreabaseball.co.kr/"><font color="#0066cc">https://koreabaseball.co.kr</font></a>)<br>
				→선수→선수조회→팀/포지션 선택 후 본인이름<br>
				→KBO정규시즌 확인(기록보기)→등록일수→<br>
				해당연도 등록일수</td>
			</tr>
			<tr>
				<td style="text-align: center;">배구</td>
				<td style="text-align: center;">경기기록증명서</td>
				<td>최근 1년간 경기기록 전체 제출</td>
			</tr>
			<tr>
				<td style="text-align: center;">럭비</td>
				<td style="text-align: center;">메치시트</td>
				<td>최근 2년간 경기기록 전체 제출</td>
			</tr>
		</tbody>
	</table>
	</li>
</ul>
</div>
</div>

<div class="layout_h3">
<h3><span style="font-size: 14px;">&nbsp;기타 유의사항<br>
<span style="font-size: 14px;">&nbsp; ㆍ&nbsp;선수등록확인서ㆍ경기실적증명서는 필수 서류(미제출시 선발제외), 대표경력증명서는 해당자만 제출</span><br>
&nbsp; ㆍ 선수등록확인서는 접수일 기준 최근 10일 이내 발행한 서류만 인정<br>
&nbsp;&nbsp;ㆍ 서류제출기간 준수(접수마감 다음날 18:00시까지)</span></h3>

<h3>※ 종목별 선수 선발기준 및 배점은 비공개(국군체육부대 예규)</h3>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html60="""<div class="layout_h3">
<h3>자격요건</h3>

<table class="table_row">
	<caption>자격요건에 대한 표이며 구분, 직종, 지원자격/선발전형에 대한내용 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_15p">
		<col class="width_auto">
	</colgroup>
	<thead>
		<tr>
			<th scope="row">구 분</th>
			<th scope="row">직 종</th>
			<th scope="row">지원자격/선발전형</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">일반</th>
			<td>
			<p>일반</p>
			</td>
			<td>
			<ul class="list">
				<li>자격증 또는 전공과 관련없이 누구나 지원가능
				<ul>
					<li>방공포/조리/군사경찰 특기 선택시 가점부여 (<strong><span style="color: rgb(0, 0, 255);">일반 직종만&nbsp;적용</span></strong>)</li>
					<li><span style="color: rgb(0, 128, 0);">'공병'은 '일반'으로 통합모집('23년 4회차(7월 입영)&nbsp;접수자부터)</span></li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th rowspan="3" scope="row">전문<br>
			기술</th>
			<td>기계/<br>
			차량정비/<br>
			화생방/<br>
			의무/<br>
			전자계산</td>
			<td>
			<ul class="list">
				<li>자격/면허 소지자(접수마감일까지 취득한 자)&nbsp;또는&nbsp;관련 직종 전공자
				<ul>
					<li>단,&nbsp;화생방 직종은 2종 보통(<span style="color: rgb(0, 0, 205);"><strong>오토면허 제외</strong></span>) 이상 운전면허 소지자(4점) 가점 부여</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>차량운전</td>
			<td>
			<ul class="list">
				<li>2종 보통 이상 운전면허증 소지자(<strong><span style="color: rgb(0, 0, 205);">오토면허 제외</span></strong>)</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>통신전자전기</td>
			<td>
			<ul>
				<li>자격증 또는 전공과 관련없이 누구나 지원가능
				<ul>
					<li>통신전자전기 관련 자격, 면허 소지자, 전공자는 배점 부여</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th rowspan="16" scope="row">전문<br>
			특기병</th>
			<td>영어어학병</td>
			<td>
			<ul class="list">
				<li><span style="font-size: 14px;">다음의 공인영어성적 기준 이상 보유자(접수마감일 기준 2년이내 성적만 인정)</span></li>
				<li>TOEIC 900점,&nbsp;<strong><span style="color: rgb(0, 0, 255);">TEPS 370점,</span></strong>&nbsp;TOEFL(IBT) 105점,&nbsp;TOEIC SPEAKING 160점, TEPS &nbsp;SPEAKING 66점 이상자</li>
				<li><strong><span style="color: rgb(0, 0, 205);">정기시험만 해당 </span></strong>(특별/수시시험은 해당되지 않음.)</li>
				<li><strong><span style="color: rgb(0, 0, 205);">'23년도 접수시기(예정)</span></strong> : '<strong><span style="color: rgb(0, 0, 205);">22.12회차('23년 3월입영), '23.2회차('23년 5월입영), '23.7회차('23년 10월입영), '23.10회차('24년 1월입영)</span></strong></li>
				<li><span style="color: rgb(0, 0, 0);">텝스(TEPS) 어학성적은 '신규 점수환산표' 적용에 따라 370점으로 기준변경 ('22</span>년 1회차('22년 4월입영자)&nbsp;부터 적용)</li>
			</ul>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; →&nbsp;접수시기는 공군 공지사항 '23년도 모집일정 안내' 참조.<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; → 상기 모집일정은 사정에 따라 변경될 수 있음.
			<ul class="list">
				<li>1차 : 모집계획 대비 3배수 선발
				<ul class="list">
					<li>출결+가산점 합계 고득점자 순(동점자 : 가산점 &gt; 출결 &gt; 생년월일 순)</li>
				</ul>
				</li>
				<li>2차 : 1차전형 선발자에 한하여 공군본부의 특별전형 실시
				<ul class="list">
					<li>필기(60점) :&nbsp;영어→한글(3개문항) 30점, 한글→영어(3개문항) 30점</li>
					<li>구술(15점) : 녹음된 영어지문 및 한글지문 통역(3개문항-문제당 5점)</li>
					<li>면접(25점) : 면접태도(5점), 표현력(5점), 학교생활(5점), 대인관계역량(5점), 의지/정신력(5점)</li>
				</ul>
				</li>
				<li><span style="color: rgb(0, 0, 255);">실기전형(2차 전형) 결과 동점일 경우 구술, 필기 평가 우수자 선발</span></li>
				<li><span style="color: rgb(0, 0, 255);">활용분야 :&nbsp; 영어어학병은 전 특기로 분류되며, 주로 해당특기 행정업무와 통/번역 업무 수행함.</span></li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>의장병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음의 기준을 모두 만족하는 자
				<ul>
					<li>신장 : 180cm 이상</li>
					<li>체중 : 65kg ~ 85kg</li>
					<li>시력 : <span style="color: rgb(0, 0, 255);">교정시력 0.7이상</span><span style="font-size: 12px;">(안경 착용 후 0.7이상인 자도 지원가능, 렌즈착용 불가자는 지원할수 없음)</span></li>
					<li>문신 : 반팔 셔츠 착용시 문신시 보이지 않는 자</li>
					<li>체력 : 팔굽혀펴기 15회 이상(1분), 윗몸일으키기 19회 이상(1분), 쪼그려뛰기 10회 이상(1분)</li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 : 지원자 전원선발</li>
					<li>2차 : 공군 특별전형(체력 75점+면접 25점)</li>
					<li>
					<div data-hjsonver="1.0" data-jsonlen="6651">최종 : 공군 특별전형 평가결과 합격자에 한하여 최종선발 대상에 포함됨</div>
					</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>군악병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음 자격요건 중 어느 한가지 이상 충족하는 자
				<ul>
					<li>지정곡(초견악보) 및 자유곡 연주 가능자</li>
					<li>지원파트 관련학과 대학 전공자</li>
					<li>고등학교(중학교) 관악부 및 동아리(군악대 모집파트) 활동자</li>
					<li>예술고등학교<span style="font-size: 11px;">(음악, 무용, 발레 등)</span> 전공자 : <span style="font-size: 12px;">선발 시만 지원자격 공고</span></li>
					<li>지원파트 연주 및 실무 경력 1년 이상자<span style="font-size: 12px;"> </span></li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 : 지원자 전원선발</li>
					<li>2차 : 공군 특별전형(실기(전공별 자유곡 1곡, 초견연주 평가) 75점+면접 25점)</li>
					<li>
					<div data-hjsonver="1.0" data-jsonlen="7608">최종 : 공군 특별전형 평가결과 합격자에 한하여 최종선발 대상에 포함됨</div>
					</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>군견관리병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 애완, 축산관련 자격면허 소지자 또는 전공자</li>
				<li>선발전형
				<ul class="list">
					<li>1차 : 출결+가산점의 합계 고득점자 순 300% 선발</li>
					<li>2차 : 공군 특별전형(전공/경력 35점+자격 40점+면접 25점)</li>
					<li>
					<div data-hjsonver="1.0" data-jsonlen="6671">최종 : 공군 특별전형 평가결과 합격자에 한하여 최종선발 대상에 포함됨</div>
					</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>정보보호병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음 자격요건 중 한가지 이상을 충족하는 자
				<ul>
					<li>전공
					<ul>
						<li>4년제 대학교 또는 전문대학에서 정보보호 및 컴퓨터(전산) 관련학과 전공자 <font color="#0000ff">(1년 수료 이상)</font></li>
						<li>고등학교 졸업자&nbsp;중 정보보호 또는 컴퓨터(전산)학과 전공자</li>
					</ul>
					</li>
					<li>자격증
					<ul>
						<li>정보보호 : 정보보안기사·산업기사, 정보보호전문가, 디지털포렌식전문가 등</li>
						<li>정보기술 : 정보처리기사·산업기사 등</li>
					</ul>
					</li>
					<li>업무경력 : 공공, 민간기관 정보보호 업무경력(6개월 이상자)</li>
					<li>기타
					<ul>
						<li>IT 역량지수(TOPCIT) 정기평가 300점이상 획득자</li>
						<li>BoB센터 "차세대 보안리더 양성 프로그램"과정 선발자</li>
					</ul>
					</li>
				</ul>
				</li>
				<li>선발전형
				<ul class="list">
					<li>1차 : 출결+가산점의 합계 고득점자 순 300% 선발</li>
					<li>2차 : 공군 특별전형 실시(전공 35점+자격 30점+경력 5점+전문교육 5점+면접 25점)</li>
					<li>최종 : 공군 특별전형 평가결과 합격자에 한하여 최종선발 대상에 포함됨</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>IT개발관리병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음 자격요건 중 한가지 이상을 충족하는 자
				<ul>
					<li>전공
					<ul>
						<li>대학교/전문대학의 SW 혹은 AI 관련학과 전공자 <font color="#0000ff">(1년 수료 이상)</font></li>
						<li>AI·SW 분야 석사과정 이수자</li>
					</ul>
					</li>
					<li>경력
					<ul>
						<li>AI·SW 분야 연구경력(업체 AI 연구인턴십, 대학교 연구실 경험)</li>
						<li>AI·SW 분야 실무경력 3개월 이상 보유자(공공기관/민간업체)</li>
						<li>AI·SW 관련 경진대회 수상경력 보유자(DACON, Kaggle, 기타 AI 경진대회 등)</li>
					</ul>
					</li>
					<li>기타
					<ul>
						<li>AI·SW 분야 관련 논문/특허 실적 보유자</li>
						<li>AI·SW 전문교육 이수자(Boostcamp AI Tech 과정, 소프트웨어 마에스트로 등)</li>
					</ul>
					</li>
				</ul>
				</li>
				<li>선발전형
				<ul class="list">
					<li>1차 : 출결+가산점의 합계 고득점자 순 300% 선발</li>
					<li>2차 : 공군 특별전형(전공 30점+자격 25점+연구·실무/수상경력 10점+전문교육 5점+면접 30점)</li>
					<li>최종 : 공군 특별전형 평가결과 합격자에 한하여 최종선발 대상에 포함됨</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>특수임무<br>
			군사경찰</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음의 기준을 모두 만족하는 자
				<ul>
					<li>신체조건 : <span style="color: rgb(0, 0, 255);">신체등급 1~2급, 신장 170Cm이상, 나안시력 0.8이상인 자</span></li>
					<li>무도자격 : 태권도, 검도, 유도, 합기도, 특공무술, 킥복싱 등 <span style="color: rgb(0, 0, 255);">무도 1단 이상자</span></li>
					<li>체력 : 팔굽혀펴기 40개이상(2분), 윗몸일으키기 50개이상(2분), 1.5km 달리기(7분 8초 이내)</li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 : 지원자 전원선발</li>
					<li>2차 : 공군 특별전형(자격증 30점+전공/경력 10점+체력 35점+면접 25점)</li>
					<li>최종 : 공군 특별전형 평가결과 합격자에 한하여 최종선발 대상에 포함됨</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>정훈병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 아래 자격/면허, 전공 중 한 가지 이상을 충족하는 자
				<ul>
					<li>자격/면허&nbsp;:&nbsp;사진기능사, 그래픽기술자격(GTQ) 1급/2급, 디지털영상편집 1급/2급,&nbsp;<strong>멀티미디어콘텐츠제작전문가, 컴퓨터그래픽스운용기능사, 웹디자인기능사</strong></li>
					<li>전공&nbsp;:&nbsp;사진학과, 영상학과, 멀티미디어학과, 언론정보학, 신문방송학과</li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 :&nbsp;출결+가산점의 합계 고득점자 순 300% 선발</li>
					<li>2차 : 공군 특별전형(실기 60점(사진 30, 영상 30)+서류 15점(전공 10, 자격증 5)+면접 25점)</li>
					<li>최종 : 공군 특별전형 평가결과 합격자에 한하여 최종선발 대상에 포함됨</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>콘텐츠<br>
			제작병</td>
			<td>
			<ul class="list">
				<li>지원자격 : <span style="color: rgb(0, 0, 255);">전공(대학교 4학기 수료 이상)</span><span style="color: rgb(0, 0, 0);">,</span><span style="color: rgb(0, 0, 255);"> </span>경력(실무 6개월 이상) 중 1가지 이상을 충족하는 자</li>
				<li>모집분야 (3개) : 그래픽디자인, 영상 촬영·편집, 일러스트레이션/웹툰
				<ul>
					<li><strong><font color="#0000cd">그래픽디자인</font></strong>
					<ul>
						<li>(전공) 시각, 커뮤니케이션 디자인/디지털미디어, 멀티미디어, 콘텐츠미디어 디자인 등 디자인 관련학과(대학교 4학기 수료 이상)</li>
						<li>(경력) 그래픽 디자인/브랜딩/콘텐츠 제작 등 디자인 관련분야</li>
					</ul>
					</li>
					<li><span style="color: rgb(0, 0, 205);"><strong>영상 촬영·편집</strong></span>
					<ul>
						<li>(전공) 영상/미디어학/영화 등 영상 관련학과(대학교 4학기 수료 이상)</li>
						<li>(경력) 영상/영화/편집/촬영 등 영상 관련분야</li>
					</ul>
					</li>
					<li><span style="color: rgb(0, 0, 205);"><strong>일러스트레이션/웹툰</strong></span>
					<ul>
						<li>(전공) 회화/만화/애니메이션 등 일러스트레이션 및 웹툰 관련학과(대학교 4학기 수료 이상)</li>
						<li>(경력) 웹툰/일러스트레이터/만화/편집디자인 등 관련분야</li>
					</ul>
					</li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 : 출결+가산점의 합계 고득점자 순 300%선발</li>
					<li>2차 : 공군 특별전형(전공 및 경력 40점+실습 35점+면접 25점)</li>
					<li>최종 : 공군 특별전형 평가결과 합격자에 한하여 최종선발 대상에 포함됨</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>식별<br>
			보조병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음 자격요건 중 어느 한가지 이상을 충족하는 자
				<ul>
					<li>중국어, CPT&nbsp;500 / 신 HSK 4급 이상자<span style="font-size: 12px;">(접수마감일 기준&nbsp;2년이내 성적만 인정)</span></li>
					<li>일본어, JPT 600 이상자<span style="font-size: 12px;">(접수마감일 기준&nbsp;2년이내 성적만 인정)</span></li>
					<li>러시아어, TORFL 1단계 이상자<span style="font-size: 12px;">(접수마감일 기준&nbsp;2년이내 성적만 인정)</span></li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 : 자격면허(50점) + 출결(10점) + 가산점(15점)의 합계 고득점자 순 200% 선발</li>
					<li>2차 : 병무청 면접(25점)</li>
					<li>최종 : 1차+2차 합계 고득점자 순</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>전문자격<br>
			의무병</td>
			<td>
			<ul class="list">
				<li>지원자격&nbsp;:<span style="color: rgb(0, 0, 255);"><strong>&nbsp;"</strong>약사" 면허를 취득한 자</span></li>
				<li>선발전형
				<ul>
					<li>1차 : 자격면허(50점) + 출결(10점) + 가산점(15점)의 합계 고득점자 순 200% 선발</li>
					<li>2차 : 병무청 면접(25점)</li>
					<li>최종 : 1차+2차 합계 고득점자 순</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>교육훈련<br>
			매체개발병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 전공(고졸 이상), 경력<span style="color: rgb(0, 0, 255);">(실무 1년 이상)</span>&nbsp;중 1가지 이상을 충족하는 자</li>
				<li>모집분야 (4개) : 3D모델링, 프로그램개발, 디자인, 영상/사진
				<ul>
					<li><span style="color: rgb(0, 0, 205);"><strong>3D모델링 </strong></span>
					<ul>
						<li>(전공) 산업/제품 디자인, 게임 그래픽, 건축 등 3D모델링 관련학과</li>
						<li>(경력) 산업디자인, 게임 3D모델링, 3D 모션그래픽, 건축, 설계 등 3D모델링 관련 분야(1년 이상)</li>
					</ul>
					</li>
					<li><strong><span style="color: rgb(0, 0, 205);">프로그램개발&nbsp;</span></strong>
					<ul>
						<li>(전공) 컴퓨터공학, 컴퓨터과학, 전산학, 정보통신 등 프로그램개발 관련학과</li>
						<li>(경력) 소프트웨어/어플리게이션/웹/게임/서버 개발 등 프로그램개발 관련 분야(1년 이상)</li>
					</ul>
					</li>
					<li><span style="color: rgb(0, 0, 205);"><strong>디자인 </strong></span>
					<ul>
						<li>(전공) 시각/커뮤니케이션/디지털미디어/멀티미디어/콘텐츠미디어 디자인 등 디자인 관련학과</li>
						<li>(경력) UX·UI 디자인, 그래픽 디자인, 일러스트레이션 등 디자인 관련 분야(1년 이상)</li>
					</ul>
					</li>
					<li><span style="color: rgb(0, 0, 205);"><strong>영상/사진 </strong></span>
					<ul>
						<li>(전공) 영상/시각 디자인, 영화, 콘텐츠미디어 등 영상 관련학과</li>
						<li>(경력) 촬영, 편집, 모션그래픽 등 영상 관련 분야(1년 이상)</li>
					</ul>
					</li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 : 전공(20점)+출결(5점)+경력(20점)의 합계 고득점자 순 300% 선발</li>
					<li>2차 : 공군본부면접(25점)+실습(30점)</li>
					<li>최종 : 1차+2차 합계 고득점자 순</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>비파괴검사병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음 필수 자격요건을 충족하는 자
				<ul>
					<li>자격증<strong><span style="color: rgb(0, 0, 255);"> (필수소지)</span></strong> : 비파괴검사기술사, 와전류비파괴검사기사, 초음파비파괴검사기사/산업기사/기능사,&nbsp;자기비파괴검사기사/산업기사/기능사, 침투비파괴검사기사/산업기사/기능사</li>
					<li>전공 : 금속공학과, 기계공학과, 기계과, 물리학과, 재료공학과</li>
				</ul>
				</li>
				<li>선발전형
				<ul class="list">
					<li>1차 : 자격(45점)+전공(30점)+ 출결(10점)+가산점(15점)의 합계 고득점자 순 200% 선발</li>
					<li>2차 : 병무청 면접(25점)</li>
					<li>최종 : 1차+2차 합계 고득점자 순</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>우주기상<br>
			분석병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음 자격요건 중 어느 한가지 이상을 충족하는 자
				<ul>
					<li>전공 : 천문우주학과, 우주과학과, 대기과학, 컴퓨터과학, 물리, 수학, 지구과학교육 전공자</li>
					<li>경력 : 국가기관 주관 데이터 처리 부문 수상 이력자(PHP, JSP 관련 개발 이력자 6개월 이상)</li>
				</ul>
				</li>
				<li>선발전형
				<ul class="list">
					<li>1차 : 경력(25점)+전공(25점)+자격증(25점)+출결(10점)+가산점(15점)의 합계 고득점자 순 200% 선발</li>
					<li>2차 : 병무청 면접(25점)</li>
					<li>최종 : 1차+2차 합계 고득점자 순</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>운항관리병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음 필수 자격요건을 충족하는 자
				<ul>
					<li>전공<strong><span style="color: rgb(0, 0, 255);">(필수)</span></strong> : 항공교통학, 항공운항학 관련 학과 재학 중인 자</li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 : 전공(75점)+출결(10점)+가산점(15점)의 합계 고득점자 순 200% 선발</li>
					<li>2차 : 병무청 면접(25점)</li>
					<li>최종 : 1차+2차 합계 고득점자 순</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>조리병</td>
			<td>
			<ul class="list">
				<li>지원자격 : 다음 자격요건 중 어느 한가지 이상을 충족하는 자
				<ul>
					<li>전공 : 조리 관련 분야 전공자</li>
					<li>자격 : 조리 관련 기능사급 이상 자격증 (한식, 일식, 양식, 중식)</li>
				</ul>
				</li>
				<li>선발전형
				<ul>
					<li>1차 : 자격(30점)+전공(20점)+출결(10점)+가산점(15점)의 합계 고득점자 순 200% 선발</li>
					<li>2차 : 병무청 면접(25점)</li>
					<li>최종 : 1차+2차 합계 고득점자 순</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>"""
html61="""<div class="layout_h3">
<h3>별도선발(전문특기병)</h3>
&nbsp; * 전문특기병 지원자는 타군&nbsp;및 타모집분야(특기)에 중복지원이 불가합니다.<br>
&nbsp; * 선발방법 : 종합성적이 높은 사람순으로 선발(배점기준 아래 표 참조)<br>
&nbsp; ※ 정보보호병과 CBT병은 복수국적자 지원불가 : 복수국적자는 비밀취급인가 불가로 해당 특기 분과 제외됨
<div class="table_scroll">
<table class="table_row">
	<colgroup>
		<col style="width: 10%;">
		<col style="width: 37%;">
		<col style="width: 40%;">
		<col style="width: 13%;">
	</colgroup>
	<thead>
		<tr>
			<th scope="row">특기</th>
			<th scope="col">지원자격</th>
			<th scope="col">배점기준</th>
			<th scope="col">임무</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">정보보호병</th>
			<td>
			<ul class="list">
				<li>다음 자격증 소지자
				<ul class="list" style="padding: 0px;">
					<li>국내.외 공인 정보보호자격증</li>
					<li>IT 국제공인자격증</li>
					<li>프로그래밍/기타 관련 자격증</li>
					<li>ICT 역량지수(TOPCIT) 정기평가 300점 이상</li>
				</ul>
				</li>
			</ul>
			* 세부 해당 자격증은 아래 참조
			<ul class="list">
				<li>다음 관련학과 전공자
				<ul class="list" style="padding: 0px;">
					<li>4년제 대학, 전문대학 : 정보보호, 컴퓨터, 전산 관련 학과 1년 수료이상</li>
					<li>고등학교 : 정보보호 관련 학과 졸업자</li>
				</ul>
				</li>
			</ul>
			</td>
			<td>
			<ul class="list">
				<li>자격증(30점) + 경력(20점) + 전공(50점) + 면접(100점)</li>
				<li>자격, 경력, 전공 세부배점 : 아래 참조</li>
				<li>면접 : 태도, 표현력, 학교생활, 의지력/정신력, 전문성
				<ul class="list" style="padding: 0px;">
					<li>항목별 각 20점(수 20, 우 15, 미 10, 양 5, 가 0)</li>
					<li>1개항목이라도 '가(0점)' 평가를 받거나 5개항목 합계 점수가 50점미만인 사람은 불합격</li>
				</ul>
				</li>
			</ul>
			* 동점자 처리기준 : 면접&nbsp;&gt;&nbsp;자격.면허&nbsp;&gt;&nbsp;전공&nbsp;&gt;&nbsp;경력&nbsp;&gt;&nbsp;생년월일 빠른 순</td>
			<td>사이버 보호, 서버/네트워크 관리 등</td>
		</tr>
		<tr>
			<th scope="row">CBT병</th>
			<td>
			<ul class="list">
				<li>관련 자격증 소지자, 관련 학과</li>
				<li>전공자, 관련 근무 경력자</li>
			</ul>
			* 세부 내용은 아래 참조</td>
			<td>
			<ul class="list">
				<li>자격증(30점) + 경력(30점) + 전공(40점) + 면접(100점)</li>
				<li>자격증, 경력, 전공 세부배점 : 아래 참조</li>
				<li>면접 : 태도, 표현력, 학교생활, 의지력/정신력, 전문성
				<ul class="list" style="padding: 0px;">
					<li>항목별 각 20점(수 20, 우 15, 미 10, 양 5, 가 0)</li>
					<li>1개항목이라도 '가(0점)' 평가를 받거나 5개항목 합계 점수가 50점미만인 사람은 불합격</li>
				</ul>
				</li>
			</ul>
			* 동점자 처리기준 : 면접&nbsp;&gt;&nbsp;자격.면허&nbsp;&gt;&nbsp;전공&nbsp;&gt;&nbsp;경력&nbsp;&gt;&nbsp;생년월일 빠른 순</td>
			<td>사이버 교육 교재 제작, 개선 등</td>
		</tr>
		<tr>
			<th scope="row">S/W개발병</th>
			<td>
			<ul class="list">
				<li>다음 자격증 소지자 또는 전공자
				<ul class="list" style="padding: 0px;">
					<li>자격
					<ul class="list" style="padding: 0px;">
						<li>정보처리기사(산업기사, 기능사)</li>
						<li>시각디자인기사(산업기사)</li>
						<li>웹디자인기능사</li>
					</ul>
					</li>
				</ul>
				<ul class="list" style="padding: 0px;">
					<li>전공
					<ul class="list" style="padding: 0px;">
						<li>컴퓨터공학</li>
						<li>컴퓨터시스템</li>
						<li>공학</li>
						<li>디지털미디어</li>
						<li>시각디자인</li>
						<li>멀티미디어</li>
						<li>전산학</li>
					</ul>
					</li>
				</ul>
				</li>
			</ul>
			</td>
			<td>
			<ul class="list">
				<li>자격(30점) + 경력(30점) + 전공(40점) + 면접(100점)</li>
				<li>자격, 경력, 전공 세부배점 : 아래 참조</li>
				<li>면접 : 태도, 표현력, 학교생활, 의지력/정신력, 전문성
				<ul class="list" style="padding: 0px;">
					<li>항목별 각 20점(수 20, 우 15, 미 10, 양 5, 가 0)</li>
					<li>1개항목이라도 '가(0점)' 평가를 받거나 5개항목 합계 점수가 50점미만인 사람은 불합격</li>
				</ul>
				</li>
			</ul>
			* 동점자 처리기준 : 면접&nbsp;&gt;&nbsp;자격.면허&nbsp;&gt;&nbsp;전공&nbsp;&gt;&nbsp;경력&nbsp;&gt;&nbsp;생년월일 빠른 순</td>
			<td>소프트웨어 개발</td>
		</tr>
		<tr>
			<th scope="row">신기술융합<br>
			연구병</th>
			<td>
			<ul class="list">
				<li>다음 자격요건 중 하나 이상 충족하는 사람</li>
				<li>자격
				<ul class="list" style="padding: 0px;">
					<li>로봇/신소재/IT 관련 국내외 공인 자격증 소지자</li>
					<li>ICT역량지수(TOPCIT) 정기평가 400점 이상 획득자</li>
				</ul>
				</li>
				<li><strong><u>전공: 관련학과 대학 3학년 이상 재학 또는 졸업자 </u></strong>(세부 전공/자격 목록은 아래 참조)</li>
			</ul>
			</td>
			<td>
			<ul class="list">
				<li>자격(30점)+전공(50점)+경력(20점)+면접(100점)<br>
				* 항목별 세부배점 : 아래 참조</li>
				<li>면접 : 태도, 표현력, 학교생활, 의지력/정신력, 전문성
				<ul class="list" style="padding: 0px;">
					<li>항목별 각 20점(수 20, 우 15, 미 10, 양 5, 가 0)</li>
					<li>1개항목이라도 '가(0점)' 평가를 받거나 5개항목 합계 점수가 50점미만인 사람은 불합격</li>
				</ul>
				</li>
			</ul>
			* 동점자 처리기준 : 면접&nbsp;&gt;&nbsp;자격.면허&nbsp;&gt;&nbsp;전공&nbsp;&gt;&nbsp;경력&nbsp;&gt;&nbsp;생년월일 빠른 순</td>
			<td>사물/만물<br>
			인터넷 연구병,<br>
			첨단센서<br>
			연구병,<br>
			신소재연구병,<br>
			무인로봇<br>
			연구병,<br>
			인공지능<br>
			연구병,<br>
			양자정보<br>
			연구병,<br>
			신추진연구병,<br>
			가상/증강현실연구병</td>
		</tr>
		<tr>
			<th scope="row">빅데이터<br>
			분석병</th>
			<td>
			<ul class="list">
				<li>자격
				<ul class="list" style="padding: 0px;">
					<li>IT 관련 국내외 공인 자격증 소지자</li>
					<li>ICT역량지수(TOPCIT) 정기평가 400점 이상 획득자</li>
				</ul>
				</li>
				<li>전공 :<span style="color: rgb(0, 0, 0);"><strong> IT(분류) 전 학과(소프트웨어학과, 컴퓨터공학과, 정보통신공학과, 인공지능학과 등) 3학년 이상 재학 또는 졸업자</strong></span></li>
			</ul>
			</td>
			<td>
			<ul class="list">
				<li>자격(30점)+전공(50점)+경력(20점)+면접(100점)<br>
				* 항목별 세부배점 : 아래 참조</li>
				<li>면접 : 태도, 표현력, 학교생활, 의지력/정신력, 전문성
				<ul class="list" style="padding: 0px;">
					<li>항목별 각 20점(수 20, 우 15, 미 10, 양 5, 가 0)</li>
					<li>1개항목이라도 '가(0점)' 평가를 받거나 5개항목 합계 점수가 50점미만인 사람은 불합격</li>
				</ul>
				</li>
			</ul>
			* 동점자 처리기준 : 면접&nbsp;&gt;&nbsp;자격.면허&nbsp;&gt;&nbsp;전공&nbsp;&gt;&nbsp;경력&nbsp;&gt;&nbsp;생년월일 빠른 순</td>
			<td>빅데이터<br>
			분석병</td>
		</tr>
		<tr>
			<th scope="row">전문의무병</th>
			<td>
			<ul class="list">
				<li>간호사, 임상병리사, 방사선사, 물리치료사, 약사, <span style="color: rgb(0, 0, 0);">응급구조사 1급 면허 보유자</span></li>
			</ul>
			* 상기 면허 보유 필수<br>
			(관련 학과 전공자라 하더라도 상기 면허 미보유자는 지원불가 / 일반의무병은 가능) (일반의무병은 일반기술/전문 기술병 으로 지원 : '의무' 계열 선택)</td>
			<td>
			<ul class="list">
				<li>경력(80점) + 고교출결(20점) + 면접(100점)</li>
				<li>경력, 고교출결 세부배점 : 아래 참조</li>
				<li>면접 : 태도, 표현력, 학교생활, 의지력/정신력, 전문성
				<ul class="list" style="padding: 0px;">
					<li>항목별 각 20점(수 20, 우 15, 미 10, 양 5, 가 0)</li>
					<li>1개항목이라도 '가(0점)' 평가를 받거나 5개항목 합계 점수가 50점미만인 사람은 불합격</li>
				</ul>
				</li>
			</ul>
			* 동점자 처리기준 : 면접&nbsp;&gt;&nbsp;경력&nbsp;&gt;&nbsp;출결&nbsp;&gt;&nbsp;생년월일 빠른 순</td>
			<td>군의관/간호장교 보좌,<br>
			의료보조</td>
		</tr>
		<tr>
			<th scope="row">지식<br>
			재산<br>
			관리병</th>
			<td>
			<ul class="list">
				<li>자격
				<ul class="list" style="padding: 0px;">
					<li>변리사 자격증 소지자(최종시험 합격자 포함)</li>
					<li><span style="color: rgb(0, 0, 255);">관련분야 1년 이상 근무경력자<br>
					* 관련분야<br>
					&nbsp;&nbsp;1. 특허법인(명세사, 도면사)<br>
					&nbsp;&nbsp;2. 선행기술조사기관 등 지식 재산 관련업종 </span></li>
					<li>지식재산 능력시험(IPAT) 3급이상 소지자</li>
					<li><span style="color: rgb(0, 0, 255);">지식재산권(특허/실용신안) 1건 이상 단독출원 및 등록자 </span>(법정대리인 예외)</li>
					<li>지식재산 관련학과 4학기(2년) 이상 이수자 (관련학과 : 지식재산학과, 발명특허학과, 지적재산권학과)</li>
				</ul>
				</li>
			</ul>
			</td>
			<td>
			<ul class="list">
				<li>자격(15점) + 전공(85점) + 면접(100점)</li>
				<li>자격, 전공 세부배점 : 아래 참조</li>
				<li>면접 : 태도, 표현력, 학교생활, 의지력/정신력, 전문성
				<ul class="list" style="padding: 0px;">
					<li>항목별 각 20점(수 20, 우 15, 미 10, 양 5, 가 0)</li>
					<li>1개항목이라도 '가(0점)' 평가를 받거나 5개항목 합계 점수가 50점미만인 사람은 불합격</li>
				</ul>
				</li>
			</ul>
			* 동점자 처리기준 : 면접&nbsp;&gt;&nbsp;자격&nbsp;&gt;&nbsp;전공&nbsp;&gt;&nbsp;생년월일 빠른 순</td>
			<td>지식재산권<br>
			보호, 관리 등</td>
		</tr>
		<tr>
			<th scope="row">인공지능(AI)<br>
			개발특기병</th>
			<td>
			<ul class="list">
				<li>자격
				<ul class="list" style="padding: 0px;">
					<li>파이썬마스터 1급, 빅데이터분석기사, 데이터분석(준)전문가, SQL전문가, SQL개발자, IT국제공인 자격증(OCP, OCM)</li>
					<li>ICT 역량지수(TOPCIT) 정기평가 400점 이상 획득자</li>
				</ul>
				</li>
				<li>전공 : 컴퓨터공학과, 컴퓨터시스템공학, 인공지능학과, 인공지능학부, AI융합학부, 인공지능융합전공, 인공지능융합학부, AI시스템과, AI학과, 인공지능공학과 등 컴퓨터 사이언스 및 인공지능 관련 학과 3학년 이상 재학자 및 졸업자</li>
			</ul>
			</td>
			<td>
			<ul class="list">
				<li>자격증(20점) + 경력(40점) + 전공(40점)</li>
				<li>자격증, 경력, 전공 세부배점 : 아래 참조</li>
				<li>면접 : 태도, 표현력, 학교생활, 의지력/정신력, 전문성
				<ul class="list" style="padding: 0px;">
					<li>항목별 각 20점(수 20, 우 15, 미 10, 양 5, 가 0)</li>
					<li>1개항목이라도 '가(0점)' 평가를 받거나 5개항목 합계 점수가 50점미만인 사람은 불합격</li>
				</ul>
				</li>
			</ul>
			* 동점자 처리기준 : 면접&nbsp;&gt;&nbsp;자격.면허&nbsp;&gt;&nbsp;전공&nbsp;&gt;&nbsp;경력&nbsp;&gt;&nbsp;생년월일 빠른 순</td>
			<td>인공지능체계 개발 보좌</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h4">
<h4>정보보호병 지원가능 자격증 세부내역</h4>

<div class="table_scroll">
<table class="table_col">
	<tbody>
		<tr>
			<td style="text-align: center;">국내.외 공인 정보보호자격증</td>
			<td>정보시스템보안전문가(CISSP), 사이버포렌식전문가(CCFP), 정보보호관리사(CISM), 정보시스템감시사(CISA),<br>
			정보보안기사/산업기사, 디지털포렌식전전문가1/2급, 인터넷보안전문가1/2급, 정보보안관리사(ISM),<br>
			해킹보안전문가1/2급, 윤리적해커인증(CEH), 정보보호관리체계(ISMS) 심사평가원 자격, 컴퓨터해킹포렌식수사관(CHFI)</td>
		</tr>
		<tr>
			<td style="text-align: center;">IT 국제공인자격증</td>
			<td>MCSA, MCSE, MCSD, MCT, MTA, MCAD, CCDA, CCNA, CCDP, CCNP, CCIE, SCYBER, OCA, OCP, OCPJP, OCMJD, OCM, OCMJEA, LPIC, RHIC, RHCT, SCSA, SCNA</td>
		</tr>
		<tr>
			<td style="text-align: center;">프로그래밍/기타 관련 자격증</td>
			<td>OCJP, SCJP, SCJD, WCD, 정보처리기사/산업기사, 네트워크관리사</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>정보보호병 세부배점 내역</h4>

<div class="layout_h5">
<h5>자격증</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">국내.외 공인 정보보호자격증</td>
			<td style="text-align: center;">30점</td>
		</tr>
		<tr>
			<td style="text-align: center;">IT 국제공인자격증</td>
			<td rowspan="2" style="text-align: center;">24점</td>
		</tr>
		<tr>
			<td style="text-align: center;">ICT 역량지수(TOPCIT) 정기평가 300점 이상</td>
		</tr>
		<tr>
			<td style="text-align: center;">프로그래밍/기타 관련 자격증</td>
			<td style="text-align: center;">18점</td>
		</tr>
		<tr>
			<td style="text-align: center;">미보유</td>
			<td style="text-align: center;">12점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>경력</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">공공, 민간기관 정보보호업무경력(6개월 이상)</td>
			<td rowspan="2" style="text-align: center;">20점</td>
		</tr>
		<tr>
			<td style="text-align: center;">공공, 민간기관 프로그램 개발 프로젝트 또는 프로그램/네트워크관리 등<br>
			실무경력(6개월 이상)</td>
		</tr>
		<tr>
			<td style="text-align: center;">BoB센터 “차세대 보안리더 양성 프로그램” 과정 이수자</td>
			<td rowspan="2" style="text-align: center;">16점</td>
		</tr>
		<tr>
			<td style="text-align: center;">KISA “최정예 사이버보안 인력 프로그램(K-Shield) 과정 이수자</td>
		</tr>
		<tr>
			<td style="text-align: center;">KUCIS(대학정보보호동아리) 활동 경력</td>
			<td style="text-align: center;">16점</td>
		</tr>
		<tr>
			<td style="text-align: center;">기타 사이버 관련 교육 1개 과정 또는 50시간 이상 이수자</td>
			<td style="text-align: center;">12점</td>
		</tr>
		<tr>
			<td style="text-align: center;">미보유</td>
			<td style="text-align: center;">8점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<thead>
		<tr>
			<th colspan="2" rowspan="3" scope="row">구분</th>
			<th colspan="8" scope="col">전공</th>
		</tr>
		<tr>
			<th colspan="2" scope="col">4년</th>
			<th colspan="2" scope="col">3년</th>
			<th colspan="2" scope="col">2년</th>
			<th colspan="2" scope="col">1년</th>
		</tr>
		<tr>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">대학교</th>
			<td>50</td>
			<td>48</td>
			<td>45</td>
			<td>43</td>
			<td>40</td>
			<td>38</td>
			<td>35</td>
			<td>33</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">전문대</th>
			<td><strong>3년제</strong></td>
			<td></td>
			<td></td>
			<td>48</td>
			<td>45</td>
			<td>43</td>
			<td>40</td>
			<td>38</td>
			<td>35</td>
		</tr>
		<tr>
			<td><strong>2년제</strong></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td>45</td>
			<td>43</td>
			<td>40</td>
			<td>38</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">고졸/ 비전공</th>
			<td colspan="8">&nbsp; 고졸(전공) : 43점 /&nbsp; 비전공 : 30점</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>CBT병 지원자격 세부내역</h4>

<div class="table_scroll">
<table class="table_col">
	<colgroup>
		<col class="width_10p">
		<col class="width_90p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">자격증</td>
			<td>DIAT(프레젠테이션) 상급, ITQ(한글, 한쇼) A등급, GTA 1급, &nbsp;GTQ 1급 이상,&nbsp;<br>
			DIAT(프레젠테이션) 중급,&nbsp;&nbsp;ITQ(한글, 한쇼) B등급, GTA 2급, 기계설계산업기사,<br>
			게임그래픽전문가, 전산응용기계제도기능사, 3차원그래픽 자격증(2급이상, PMC), 멀티미디어<br>
			콘텐츠제작전문가, &nbsp;웹디자인기능사, 컴퓨터그래픽스운용기능사, 영사산업기사<br>
			ICT 역량지수 (TOPCIT) 정기평가 300점 이상 획득자, 광학기기산업기사, 사진기능사, 영사기능사,<br>
			어도비ACE/ACA 국제공인자격증, 유니티 공인 인증시험, BMI 운용전문가, 디지털영상편집 1/2급</td>
		</tr>
		<tr>
			<td style="text-align: center;">전공</td>
			<td>그래픽, 디자인, 게임, 만화, 미술, 시각 디자인 관련학과<br>
			&nbsp;게임애니메이션, 기계CAD/기계설계, 컴퓨터공학, 컴퓨터과학, 소프트웨어학 등 개발관련학과<br>
			교육공학, 교육학과, 교육학 계열 학과 전문대이상, 영상 관련 학과 대학교 재학 또는 졸업자/고등학교 졸업 예정자</td>
		</tr>
		<tr>
			<td style="text-align: center;">경력</td>
			<td>그래픽, 디자인 관련 기업, 3D그래픽 게임개발 관련 법인 기업, 교육콘텐츠 업체, 영상 관련 법인기업에서 프로그램 개발 프로젝트 또는 실무경력이 있는 자</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>CBT병 세부배점 내역</h4>

<div class="layout_h5">
<h5>자격증</h5>

<div class="table_scroll">
<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">DIAT(프레젠테이션) 상급, ITQ(한글, 한쇼) A등급,&nbsp;&nbsp;GTA 1급, 기계설계산업기사, 광학기기산업기사,&nbsp;<br>
			영사산업기사,&nbsp;BMI 운용전문가 1급, 유니티 공인 인증시험(Professional, Expert)</td>
			<td style="text-align: center;">30점</td>
		</tr>
		<tr>
			<td style="text-align: center;">DIAT(프레젠테이션) 중급, ITQ(한글, 한쇼) B등급,&nbsp;GTA 2급, 게임그래픽전문가, 전산응용기계제도기능사,<br>
			멀티미디어 콘텐츠제작전문가, 웹디자인기능사, 컴퓨터그래픽스운용기능사,&nbsp;&nbsp;사진기능사, 영사기능사,<br>
			ICT 역량지수(TOPCIT) 정기평가 300점 이상 획득자, BMI 운용전문가 2급, 디지털영상편집 1급,<br>
			유니티 공인 인증시험(Associate)</td>
			<td style="text-align: center;">25점</td>
		</tr>
		<tr>
			<td style="text-align: center;">3차원 그래픽 자격증(2급이상, PMC), GTQ 1급 이상, 어도비 ACE/ACA 국제공인자격증<br>
			디지털영상편집 2급, 유니티 공인 인증시험(User)</td>
			<td style="text-align: center;">20점</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h5">
<h5>경력</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">지원자격에 적합한 기업&nbsp;중 2년 이상 근무한 자</td>
			<td style="text-align: center;">30점</td>
		</tr>
		<tr>
			<td style="text-align: center;">지원자격에 적합한 기업&nbsp;중 1년 이상 근무한 자</td>
			<td style="text-align: center;">20점</td>
		</tr>
		<tr>
			<td style="text-align: center;">지원자격에 적합한 기업&nbsp;중 1년 이하 근무한 자</td>
			<td style="text-align: center;">10점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<thead>
		<tr>
			<th colspan="2" rowspan="3" scope="row">구분</th>
			<th colspan="8" scope="col">전공</th>
		</tr>
		<tr>
			<th colspan="2" scope="col">4년</th>
			<th colspan="2" scope="col">3년</th>
			<th colspan="2" scope="col">2년</th>
			<th colspan="2" scope="col">1년</th>
		</tr>
		<tr>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">대학교</th>
			<td>40</td>
			<td>38</td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
			<td>28</td>
			<td>26</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">전문대</th>
			<td><strong>3년제</strong></td>
			<td></td>
			<td></td>
			<td>38</td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
			<td>28</td>
		</tr>
		<tr>
			<td><strong>2년제</strong></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">고졸/ 비전공</th>
			<td colspan="8">&nbsp; 고졸(전공) : 34점 /&nbsp; 비전공 : 24점</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>S/W개발병 세부배점 내역</h4>

<div class="layout_h5">
<h5>자격</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">기사 자격증</td>
			<td style="text-align: center;">30점</td>
		</tr>
		<tr>
			<td style="text-align: center;">산업기사 자격증</td>
			<td style="text-align: center;">25점</td>
		</tr>
		<tr>
			<td style="text-align: center;">기능사 자격증</td>
			<td style="text-align: center;">20점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>경력</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">S/W개발 경험 2년 이상</td>
			<td style="text-align: center;">30점</td>
		</tr>
		<tr>
			<td style="text-align: center;">S/W개발 경험&nbsp;1년 이상 ~ 2년 미만</td>
			<td style="text-align: center;">25점</td>
		</tr>
		<tr>
			<td style="text-align: center;">S/W개발 경험 1년 미만</td>
			<td style="text-align: center;">20점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<thead>
		<tr>
			<th colspan="2" rowspan="3" scope="row">구분</th>
			<th colspan="8" scope="col">전공</th>
		</tr>
		<tr>
			<th colspan="2" scope="col">4년</th>
			<th colspan="2" scope="col">3년</th>
			<th colspan="2" scope="col">2년</th>
			<th colspan="2" scope="col">1년</th>
		</tr>
		<tr>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" scope="row">대학교</th>
			<td>40</td>
			<td>38</td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
			<td>28</td>
			<td>26</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">전문대</th>
			<td><strong>3년제</strong></td>
			<td></td>
			<td></td>
			<td>38</td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
			<td>28</td>
		</tr>
		<tr>
			<td><strong>2년제</strong></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td>36</td>
			<td>34</td>
			<td>32</td>
			<td>30</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">고졸/ 비전공</th>
			<td colspan="8">&nbsp; 고졸(전공) : 34점 /&nbsp; 비전공 : 24점</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>신기술융합연구병</h4>

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<colgroup>
		<col class="width_100p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">- 기계(분류) 학과<br>
			기계공학과, 기계설계공학과, 기계시스템디자인공학과, 기계시스템학과,<br>
			에너지기계공학과, 로봇공학과, 메카트로닉스공학과, 광메카트로닉스공학과,<br>
			나노메카트로닉스공학과<br>
			- 화학(분류) 학과<br>
			화학공학과, 신소재공학과, 신소재화공시스템공학과, 정보전자신소재공학과,<br>
			융합에너지신소재공학과, 화공신소재공학과, 나노신소재공학과,<br>
			나노소재전공, 바이오시스템소재공학과, 미래에너지공학과,<br>
			고분자공학과, 응용화학공학과, 청정융합에너지공학과<br>
			- IT(분류) 학과<br>
			컴퓨터공학과, 컴퓨터소프트웨어학과, 컴퓨터과학과, 컴퓨터전자시스템공학과,<br>
			빅데이터경영통계전공, 데이터통계학과, 정보컴퓨터공학과, 인공지능학과,<br>
			소프트웨어학과, 데이터사이언스학과, 전자전기공학과, 전자전기컴퓨터공학과,<br>
			사이버국방학과, 국방정보공학과, 해양융합과학·공학과, 모바일시스템공학과,<br>
			경영정보학과, 임베디드시스템공학과, 휴먼지능정보학과, 정보보안학과</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>자격</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">로봇기구개발기사, 로봇소프트웨어개발기사, 로봇하드웨어개발기사,<br>
			금속재료기사, 신재생에너지발전설비기사, 정보처리기사, 정보보안기사,<br>
			ICT 역량지수(TOPCIT) 정기평가 400점 이상 획득자,<br>
			리눅스마스터 1급, 데이터분석전문가(ADP), 빅데이터분석기사<br>
			IT 국제공인자격증(MCSE, OCM, CISSP, OCNA)</td>
			<td style="text-align: center;">30점</td>
		</tr>
		<tr>
			<td style="text-align: center;">금속재료산업기사, 신재생에너지발전설비산업기사, 정보처리산업기사,<br>
			정보보안산업기사, 리눅스마스터 2급, 데이터분석준전문가(ADSP),<br>
			IT 국제공인자격증(LPIC, MCSA, OCP, CISA, OCSA)</td>
			<td style="text-align: center;">25점</td>
		</tr>
		<tr>
			<td style="text-align: center;">&nbsp;IT 국제공인자격증(OCJP, OCA)</td>
			<td style="text-align: center;">20점</td>
		</tr>
		<tr>
			<td style="text-align: center;">미보유</td>
			<td style="text-align: center;">15점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="row">구분</th>
			<th colspan="2" scope="col">4년</th>
			<th colspan="2" scope="col">3년</th>
		</tr>
		<tr>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">대학교</th>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">35</td>
			<td style="text-align: center;">30</td>
			<td style="text-align: center;">25</td>
		</tr>
		<tr>
			<th scope="row">전문대(3년제)</th>
			<td></td>
			<td></td>
			<td style="text-align: center;">30</td>
			<td style="text-align: center;">25</td>
		</tr>
		<tr>
			<th scope="row">대학원(석사)</th>
			<td colspan="4">&nbsp; 수료 50점 / 재학 45점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>경력</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">&nbsp;IoT, 무인로봇, 인공지능, 빅데이터&nbsp;등 4차산업혁명 관련 시스템 개발 프로젝트 또는 실무경력이 있는 사람(1년 이상)</td>
			<td style="text-align: center;">20점</td>
		</tr>
		<tr>
			<td style="text-align: center;">&nbsp;IoT, 무인로봇, 인공지능, 빅데이터&nbsp;등 4차산업혁명 관련 시스템 개발 프로젝트 또는 실무경력이 있는 사람(3개월 이상)</td>
			<td style="text-align: center;">15점</td>
		</tr>
		<tr>
			<td style="text-align: center;">미보유</td>
			<td style="text-align: center;">10점</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>빅데이터분석병 세부배점 내역</h4>

<div class="layout_h5">
<h5>자격증</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">ICT 역량지수(TOPCIT) 정기평가 400점 이상 획득자, 데이터아키텍처 전문가(DAP, Data Architecture Professional), SQL(Structured Query Language) 전문가, 데이터분석전문가(ADP), IT국제공인자격증(MCSE, OCM, CISSP, OCNA), 정보처리기사, 리눅스마스터 1급</td>
			<td style="text-align: center;">30점</td>
		</tr>
		<tr>
			<td style="text-align: center;">데이터아키텍처 준전문가(DAsP, Data Architecture Semi-Professional), SQL(Structured Query Language) 개발자, 데이터분석 준전문가(ADsP), IT국제공인자격증(LPIC, MCSA, OCP, CISA, OCSA), 정보처리산업기사, 리눅스마스터 2급</td>
			<td style="text-align: center;">25점</td>
		</tr>
		<tr>
			<td style="text-align: center;">정보처리기능사, IT국제공인자격증(OCJP, OCA)</td>
			<td style="text-align: center;">20점</td>
		</tr>
		<tr>
			<td style="text-align: center;">미보유</td>
			<td style="text-align: center;">15점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<thead>
		<tr>
			<th rowspan="2" scope="row">구분</th>
			<th colspan="2" scope="col">4년</th>
			<th colspan="2" scope="col">3년</th>
		</tr>
		<tr>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">대학교</th>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">35</td>
			<td style="text-align: center;">30</td>
			<td style="text-align: center;">25</td>
		</tr>
		<tr>
			<th scope="row">전문대(3년제)</th>
			<td></td>
			<td></td>
			<td style="text-align: center;">30</td>
			<td style="text-align: center;">25</td>
		</tr>
		<tr>
			<th scope="row">대학원(석사)</th>
			<td colspan="4">&nbsp; 수료 50점 / 재학 45점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>경력</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">빅데이터, 인공지능, IoT 등 4차산업혁명 관련 시스템 개발 프로젝트 또는<br>
			실무경력이 있는 사람(1년 이상)</td>
			<td style="text-align: center;">20점</td>
		</tr>
		<tr>
			<td style="text-align: center;">빅데이터, 인공지능, IoT 등 4차산업혁명 관련 시스템 개발 프로젝트 또는<br>
			실무경력이 있는 사람(3개월 이상)</td>
			<td style="text-align: center;">15점</td>
		</tr>
		<tr>
			<td style="text-align: center;">미보유</td>
			<td style="text-align: center;">10점</td>
		</tr>
	</tbody>
</table>
</div>
</div>
&nbsp;

<div class="layout_h4">
<h4>전문의무병 세부배점 내역</h4>

<div class="layout_h5">
<h5>경력(개인병원 이상 임상 근무 경력/ 학교실습제외)</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">1년 이상</td>
			<td style="text-align: center;">80점</td>
		</tr>
		<tr>
			<td style="text-align: center;">6월 이상 ~ 1년 미만</td>
			<td style="text-align: center;">75점</td>
		</tr>
		<tr>
			<td style="text-align: center;">3월 이상 ~ 6월 미만</td>
			<td style="text-align: center;">70점</td>
		</tr>
		<tr>
			<td style="text-align: center;">3월 미만</td>
			<td style="text-align: center;">65점</td>
		</tr>
		<tr>
			<td style="text-align: center;">없음</td>
			<td style="text-align: center;">60점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>출결</h5>

<table class="table_row">
	<tbody>
		<tr>
			<td style="text-align: center;">구분</td>
			<td style="text-align: center;">결석 0일</td>
			<td style="text-align: center;">결석 1~2일</td>
			<td style="text-align: center;">결석 3~5일</td>
			<td style="text-align: center;">결석 6일이상</td>
			<td style="text-align: center;">비 고</td>
		</tr>
		<tr>
			<td style="text-align: center;">점수</td>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">17</td>
			<td style="text-align: center;">14</td>
			<td style="text-align: center;">11</td>
			<td style="text-align: center;">고교3년간 누계 적용</td>
		</tr>
	</tbody>
</table>
</div>
</div>
&nbsp;

<div class="layout_h4">
<h4>지식재산관리병 세부배점</h4>

<div class="layout_h5">
<h5>자격</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">변리사 자격증 소지자(최종시험 합격자 포함)</td>
			<td style="text-align: center;">15</td>
		</tr>
		<tr>
			<td style="text-align: center;"><span style="color: rgb(0, 0, 255);">관련분야 1년 이상 근무경력자</span></td>
			<td style="text-align: center;"><span style="color: rgb(0, 0, 255);">10</span></td>
		</tr>
		<tr>
			<td style="text-align: center;">지식재산 능력시험(IPAT) 1급 소지자</td>
			<td style="text-align: center;">10</td>
		</tr>
		<tr>
			<td style="text-align: center;">지식재산 능력시험(IPAT) 2급 또는 3급&nbsp;소지자</td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><span style="color: rgb(0, 0, 255);">지식재산권(특허/실용신안) 1건 이상 단독출원<br>
			및 등록자 (법정대리인 제외)</span></td>
			<td style="text-align: center;"><span style="color: rgb(0, 0, 255);">6</span></td>
		</tr>
	</tbody>
</table>
</div>
&nbsp;

<div class="layout_h5">
<h5>전공</h5>

<table class="table_col">
	<thead>
		<tr>
			<th colspan="2" rowspan="3" scope="row">구분</th>
			<th colspan="8" scope="col">전공</th>
		</tr>
		<tr>
			<th colspan="2" scope="col">4년</th>
			<th colspan="2" scope="col">3년</th>
			<th colspan="2" scope="col">2년</th>
			<th colspan="2" scope="col">1년</th>
		</tr>
		<tr>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th colspan="2" rowspan="1" scope="row">대학교</th>
			<td>85</td>
			<td>84</td>
			<td>83</td>
			<td>82</td>
			<td>81</td>
			<td>80</td>
			<td>80</td>
			<td>80</td>
		</tr>
		<tr>
			<th rowspan="2" scope="row">전문대</th>
			<td><strong>3년제</strong></td>
			<td></td>
			<td></td>
			<td>83</td>
			<td>82</td>
			<td>81</td>
			<td>80</td>
			<td>80</td>
			<td>80</td>
		</tr>
		<tr>
			<td><strong>2년제</strong></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td>81</td>
			<td>80</td>
			<td>80</td>
			<td>80</td>
		</tr>
		<tr>
			<th colspan="2" scope="row">고졸/ 비전공</th>
			<td colspan="8">&nbsp;&nbsp;79점</td>
		</tr>
	</tbody>
</table>
</div>
</div>

<div class="layout_h4">
<h4>인공지능(AI)개발특기병 세부 배점(서류 100)</h4>

<div class="layout_h5">
<h5>자격(20)</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">파이썬마스터 1급, 빅데이터분석기사, 데이터분석전문가, SQL전문가, ICT 역량지수(TOPCIT)정기평가 400점 이상 획득자</td>
			<td style="text-align: center;">20</td>
		</tr>
		<tr>
			<td style="text-align: center;">데이터분석 준전문가, SQL개발자, IT국제공인 자격증(OCP, OCM)</td>
			<td style="text-align: center;">15</td>
		</tr>
		<tr>
			<td style="text-align: center;">보유 없음</td>
			<td style="text-align: center;">10</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>경력(40)</h5>

<table class="table_col">
	<colgroup>
		<col class="width_80p">
		<col class="width_20p">
	</colgroup>
	<tbody>
		<tr>
			<td style="text-align: center;">구 분</td>
			<td style="text-align: center;">배 점</td>
		</tr>
		<tr>
			<td style="text-align: center;">빅데이터, 인공지능 개발 프로젝트 및 실무경력이 있는 자(3년 이상)</td>
			<td style="text-align: center;">40점</td>
		</tr>
		<tr>
			<td style="text-align: center;">빅데이터, 인공지능 개발 프로젝트 및 실무경력이 있는 자(2~3년 미만)</td>
			<td style="text-align: center;">35점</td>
		</tr>
		<tr>
			<td style="text-align: center;">빅데이터, 인공지능 개발 프로젝트 및 실무경력이 있는 자(1~2년 미만)</td>
			<td style="text-align: center;">30점</td>
		</tr>
		<tr>
			<td style="text-align: center;">빅데이터, 인공지능 개발 프로젝트 및 실무경력이 있는 자(1년 미만)</td>
			<td style="text-align: center;">20점</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h5">
<h5>전공(40)</h5>

<table class="table_col">
	<thead>
		<tr>
			<th rowspan="3" scope="row">구분</th>
			<th colspan="8" scope="col">전공</th>
		</tr>
		<tr>
			<th colspan="2" scope="col">4년</th>
			<th colspan="2" scope="col">3년</th>
		</tr>
		<tr>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
			<th scope="col">수료</th>
			<th scope="col">재학</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">대학교</th>
			<td>32</td>
			<td>28</td>
			<td>24</td>
			<td>20</td>
		</tr>
		<tr>
			<th scope="row">전문대</th>
			<td></td>
			<td></td>
			<td>24</td>
			<td>20</td>
		</tr>
		<tr>
			<th scope="row">대학원(석사)</th>
			<td colspan="4">&nbsp; 수료 40점 / 재학 36점</td>
		</tr>
	</tbody>
</table>
</div>
</div>
</div>"""
html62="""<div class="layout_h3">
<h3>모집개요-취업맞춤특기병</h3>

<div class="layout_h4">
<h4>'취업맞춤특기병' 이란?</h4>

<p>고졸 이하 병역의무자가 군에 입영하기 전에 본인의 적성에 맞는 기술훈련을 받고 이와 연계된 분야의 기술병으로 입영하여 군 복무함으로써 취업 등 안정적으로 사회 진출할 수 있는&nbsp;현역병 모집분야</p>
</div>

<div class="layout_h4">
<h4>제도 장점 및 혜택</h4>

<div class="layout_h5">
<h5>입영 전</h5>

<ul class="list">
	<li>기술훈련 받는 동안 훈련비(전액 또는 일부)를 지원받을 수 있습니다.</li>
	<li>기술훈련을 마친 사람은 취업지원을 받게 되며, 취업하게 되면 24세까지 현역병 입영을 연기할 수 있습니다.</li>
	<li>입영을 원할 경우는 관련분야 기술병으로&nbsp;입영할 수 있습니다.</li>
</ul>
</div>

<div class="layout_h5">
<h5>군 복무</h5>

<ul class="list">
	<li>복무 중에는 기술훈련 받은 분야의 기술병으로 복무하며 자격 취득, 기술숙련 등 자기개발을 통해 미래를 준비할 수 있습니다.</li>
</ul>
</div>

<div class="layout_h5">
<h5>전역 후</h5>

<ul class="list">
	<li>군 복무를 마치면 고용노동부, 국가보훈부, 중소벤처기업부&nbsp;등 유관기관과 협업하여 제공하는 취업지원서비스를 받게 됩니다.</li>
</ul>
<!-- 이미지 삽입 -->

<p>※ 기술훈련과정 : 기술훈련에 처음 참여하는 사람은 취업맞춤특기병에 지원하면 고용노동부 국민취업지원제도에 참여하여 본인 적성에 맞는 훈련을 받게 됩니다. 이때 취업맞춤특기병을 먼저 지원하지 않았더라도 이미 기술훈련(*아래 훈련과정 해당)을 받고 있거나 마친 사람의 경우도 훈련을 수료하면 취업맞춤특기병에 지원이 가능합니다.</p>

<p>* 훈련과정 : 국가기간·전략산업 직종훈련, 중소기업친화직종훈련, 국가인적자원개발 컨소시엄 채용예정자훈련, 폴리텍 기능사 양성과정 훈련, 내일배움카드제 훈련 중 일부, 일학습병행제, 내일이룸학교 등<br>
<br>
※ 직업계고(마이스터고, 특성화고, 일반고 직업계열) 학생은 기술훈련을 받지&nbsp;않아도 전공학과 분야로 지원 가능합니다.(단, 육군 23개 특기에 한함)</p>
</div>
</div>
</div>"""
html63="""
<h3>모집안내-지원자격</h3>

<table class="table_row">
	<caption>모집안내-지원자격에 관한표이며 연령, 학력, 신체, 기술훈련, 선발제외대상에 관한내용을 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_auto">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">연령</th>
			<td>지원서 접수년도 기준 18세이상 24세이하 ('24년 기준 : '00.1.1 ~ '06.12.31 출생자)</td>
		</tr>
		<tr>
			<th scope="row">학력</th>
			<td>
			<ul class="list">
				<li>고등학교 졸업이하 학력소지 또는 교육부장관이 인정하는 동등 학력을 소지한 사람
				<ul>
					<li>고교 재학 중인 사람은 지원 제한, 다만 상급학교를 진학하지 아니한 경우는 졸업 하는 해 1월 1일부터 지원 가능, 대학중퇴자는 지원 가능&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: rgb(0, 0, 205);">&nbsp;&nbsp;</span>&nbsp;</li>
				</ul>
				</li>
			</ul>
			&nbsp;<br>
			&nbsp; * 학점은행제를 통한 전문학사 학위취득자 및 폴리텍대학, 전문대, 사이버대, 방통대&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 재학ㆍ졸업자&nbsp;지원 가능&nbsp;&nbsp;&nbsp;&nbsp;<br>
			&nbsp;&nbsp;* 기초생활수급자, 차상위계층, 한부모가족지원대상은 대학졸업(예정)자도 참여 가능</td>
		</tr>
		<tr>
			<th scope="row">신체</th>
			<td>
			<div class="layout_h5">
			<h3><span style="color: rgb(105, 105, 105);"><span style="font-size: 14px;">병역판정검사 결과 신체등급&nbsp;1∼4급자로서 현역병 입영대상인 사람</span></span></h3>
			<ul class="list">
				<li>모집특기별 신체제한 사항의 사유에 해당되지 아니한 사람
				<ul>
					<li>병역판정(지원)검사를 받지 아니한 사람은 신체검사 별도 실시</li>
					<li>다만, 18세자는 18세에 입영하게 될 경우&nbsp;18세에 현역병지원 병역판정검사를 실시(신체등급&nbsp;5~6급자는 전시근로역&nbsp;또는 병역면제 인정), 19세 이후에 입영하게 될 경우는 18세 병역판정검사를 보류하고 19세에 가급적 빠른 일자를 정하여 병역판정검사 실시</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">기술훈련</th>
			<td>
			<p>기술훈련에 처음 참여하는 사람은 취업맞춤특기병에 지원하면 고용노동부 국민취업지원제도에 참여하여 본인 적성에 맞는 훈련을 받게 됩니다. 이때 취업맞춤특기병을 먼저 지원하지 않았더라도 이미 기술훈련(*아래 훈련과정 해당)을 받고 있거나 마친 사람의 경우도 훈련을 수료하면 취업맞춤특기병에 지원이 가능합니다.</p>
			<p>&nbsp;*&nbsp;훈련과정: 국가기간·전략산업직종훈련, 중소기업친화직종훈련, 국가인적자원개발컨소시엄 채용예정훈련, 폴리텍 기능사양성과정 훈련, 내일배움카드제 훈련 중 일부, 일학습병행제, 내일이룸학교 등 국가기관 또는 지방자치단체에서 주관하는 직업훈련 과정</p>
			<ul>
				<li><strong>기술훈련 참여 희망자 : </strong>지원 → 상담 → 훈련 → 취업 또는 입영</li>
				<li><strong>기술훈련 참여 중인 자 : </strong>지원 → 훈련 → 취업 또는 입영</li>
				<li><strong>기술훈련 수료자 :</strong> 지원 → 취업 또는 입영</li>
			</ul>
			<br>
			* 직업계고(마이스터고, 특성화고, 일반고 직업계열) 학생은 기술훈련을 받지&nbsp;않아도 전공학과 분야로 지원 가능합니다.(단, 육군 23개 특기에 한함)
			<dl>
			</dl>
			</td>
		</tr>
		<tr>
			<th scope="row"><span style="font-size: 12px;">선발제외대상</span></th>
			<td>
			<div class="layout_h5">
			<h3><span style="color: rgb(105, 105, 105);"><span style="font-size: 14px;">아래 사항에 해당되는 경우에는 취업맞춤특기병 선발을 제외</span></span></h3>
			<ul class="list">
				<li>정해진 기한 내 상담 및 기술훈련 등을 받지 아니한 경우
				<ul>
					<li>연락 두절 또는 고의적으로 상담을 회피하는 등으로 상담이 곤란한 경우</li>
					<li>지원서 접수 후 지방병무청 전문상담관을 대면하여 상담, 지원확인서 발급일로부터 1월이내 고용센터 전문상담원을 방문상담 하여야 함</li>
					<li>지원서 접수일로 부터 6월을 초과하였음에도 기술훈련이 시작되지 않고 있으며, 기술훈련을 받고자 하는 의사가 없거나 고의적으로 지연시키는 경우</li>
				</ul>
				</li>
				<li>범죄경력 조회결과 아래 사항에 해당되는 사람
				<ul>
					<li>징역 또는 금고의 형의 실형(집행유예 포함)을 선고받은 사람</li>
					<li>수사·재판 중에 있거나 처분미상으로 통보된 사람으로서 기술훈련 시작일 까지 수사종결처분·결정 또는 재판이 확정되지 아니하였거나 처분결과가 판명되지 아니한 사람</li>
				</ul>
				</li>
				<li>지원서를 허위로 작성하거나 제출서류가 허위 또는 위조로 확인된 사람</li>
			</ul>
			</div>
			</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;※ 「 대체역의 편입 및 복무 등에 관한 법률 」 에 따라 대체역 편입원을 제출한 사람은 지원을 제한합니다.<br>
<br>
취업맞춤특기병 모집특기 목록 <span class="button down white2 ml10px"><a href="/cmfileDown.do?gtfile_no=184">다운로드</a><a href="/cmfileView.do?gtfile_no=184" target="_blank">미리보기</a></span><br>
<br>
&nbsp;</p>

<div class="layout_h3">
<h3>지원서 접수</h3>

<table class="table_row">
	<caption>지원서 접수에 관한표이며 접수기간, 접수처, 참고사항에 대한내용을 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_auto">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">접수기간</th>
			<td>1월 ~ 12월</td>
		</tr>
		<tr>
			<th scope="row">접수처</th>
			<td>
			<dl class="list">
				<dt>인터넷 접수 :</dt>
				<dd>병무청 홈페이지→ 병무민원포털 → 군지원→ 지원서작성 및 수정취소 → 취업맞춤특기병 모집</dd>
				<dt>서면(방문) 접수 :</dt>
				<dd>지방병무청 군지원센터(병역진로설계지원센터)</dd>
			</dl>
			</td>
		</tr>
		<tr>
			<th scope="row">참고사항</th>
			<td>
			<ul class="list">
				<li>지원자는 지원서 작성 시 원하는 기술훈련·군복무 희망분야 등을 기재</li>
				<li>지원 시 선택한 입영시기·부대·특기 등은 입영하는 해 입영계획에 따라 변경될 수 있음을 유의</li>
				<li>현역병(징집병) 입영일이 결정된 사람은 입영일 30일 전까지 지원가능하며, 이 때 지원자는 입영일자&nbsp;연기 신청서를 병적지 지방병무청에 제출하여야 함</li>
				<li>타 군에 지원하여 합격한 사람은 지원을 제한</li>
				<li>지원서 접수취소는 기술훈련 시작 전까지 병무청 홈페이지 →&nbsp;병무민원포털 → 군지원→ 지원서 작성·수정·취소에서 접수취소 가능</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3>구비서류</h3>

<ul class="list">
	<li>취업맞춤특기병 지원서 <span class="button down white2 ml10px"><a href="/cmfileDown.do?gtfile_no=154">다운로드</a><a href="/cmfileView.do?gtfile_no=154" target="_blank">미리보기</a></span></li>
	<li>최종학교 졸업증명서 또는 최종학년 재학·수료·휴학·퇴학증명서 등 1부</li>
	<li>훈련기관장이 발행하는 '훈련참여(수료)확인서' 1부(기술훈련을 마친 사람만 제출) <span class="button down white2 ml10px"><a href="/cmfileDown.do?gtfile_no=153">다운로드</a><a href="/cmfileView.do?gtfile_no=153" target="_blank">미리보기</a></span>
	<ul>
		<li>&nbsp;'훈련기관'이란, 직업전문학교·기술학원 등 국가기관 및 지방자치단체가 주관하는 공공 또는 민간위탁 기술훈련기관을 말함</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h3">
<h3>입영</h3>

<ul class="list">
	<li>기술훈련을 마친 사람은 해당 분야로 취업하거나 입영할 수 있습니다.
	<ul>
		<li><strong>'先취업 後입영' 하는 경우</strong></li>
		<li>기술훈련 수료 후 6월 이내 취업한 사람은 24세까지 입영연기, 연기기간 중 입영 신청하면 입영 가능(가급적 원하는 시기 반영, 모집계획 범위 내)<br>
		&nbsp;</li>
		<li>미취업자는 정해진 일자에 입영(입영일은 훈련수료 다음 달부터 6월 후 3월 이내)</li>
		<li><strong>'先입영 後취업' 하는 경우</strong></li>
		<li>「조기입영 신청서」제출 <span class="button down white2 ml10px"><a href="/cmfileDown.do?gtfile_no=186">다운로드</a><a href="/cmfileView.do?gtfile_no=186" target="_blank">미리보기</a></span>, 기술훈련 수료일로부터 6월 내의 일자에 입영(모집계획 범위 내)</li>
	</ul>
	</li>
	<li>취업맞춤특기병으로 선발되어 입영통지된 사람은 병무청 홈페이지 또는 귀하의 e-mail에서 현역병입영통지서를 출력 후 통지서를 지참하고 정해진 입영일자·부대로 입영합니다.</li>
	<li>만일, 부득이한 사유로 선발취소를 원하는 경우에는 병무청 홈페이지 →&nbsp;병무민원포털 → 군지원→ 선발취소 및 입영연기 등 민원&nbsp;→ 선발취소 신청에서 인터넷으로 취소 신청할 수 있습니다.(필요시 관련증빙서류 제출)</li>
	<li>부득이한 사유는 아래와 같습니다.
	<ul>
		<li>질병 또는 심신장애 사유로&nbsp;2주 이상의 치유기간이 필요하다고 인정되는 경우</li>
		<li>본인의 직계 존·비속, 배우자, 형제자매 또는 세대구성원의 위독, 사망 등으로 하여 본인이 아니면 가사정리가 어렵다고 인정되는 경우</li>
		<li>천재지변 기타 재난을 당하여 본인이 아니면 이를 처리하기 어렵다고 인정되는 경우</li>
		<li>최종 합격자 발표일 전날까지 각 군에서 모집하는 장교, ·부사관, 병, 의무소방원, 전투경찰순경에 지원하여 수험결과를 기다리고 있거나 또는 선발시험에 합격한 경우</li>
		<li>취업맞춤특기병 선발취소를 원하는 경우</li>
	</ul>
	</li>
</ul>
</div>

<div class="layout_h3">
<h3>복무</h3>

<table class="table_row">
	<caption>복무에 관한표이며 입영시기, 입영부대, 복무분야, 유의사항에 관한 내용을 제공</caption>
	<colgroup>
		<col class="width_20p">
		<col class="width_auto">
	</colgroup>
	<tbody>
		<tr>
			<th scope="row">입영시기</th>
			<td>1월 ~ 12월<br>
			입영일자는 매년 수립되는 현역병 입영계획 및 개인별 기술훈련 수료시기, 취업 시기 등에 따라 다름</td>
		</tr>
		<tr>
			<th scope="row">입영부대</th>
			<td>육군훈련소(충남 논산)</td>
		</tr>
		<tr>
			<th scope="row">복무분야</th>
			<td>개인별 기술훈련 분야와 연관된 기술특기(건설·정비·기계·통신·전자 등 57개 특기)</td>
		</tr>
		<tr>
			<th scope="row">유의사항</th>
			<td>취업맞춤특기병으로 선발되어 입영한 사람 중 신체적 결함 또는 해당 특기에 대한 직무수행 능력이 저조하거나 각종 사고자 등 부대임무상 특기조정이 불가피한 경우는 최초 선발된 특기와 다른 군사특기로 재분류되어 복무하게 됩니다.</td>
		</tr>
	</tbody>
</table>
</div>

<div class="layout_h3">
<h3>전역후</h3>

<ul class="list">
	<li>군 복무를 마치면 고용노동부, 국가보훈부, 중소벤처기업부&nbsp;등 유관기관과 협업하여 제공하는 취업지원서비스를 받게 됩니다.</li>
</ul>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
html64="""<div class="layout_h3">
<h3>모집절차</h3>

<p class="indent">01. 취업맞춤특기병지원(인터넷,방문)<br>
&nbsp;지원서 접수<br>
• 인터넷 :병무청 홈페이지 병무민원포털(www.mma.go.kr)<br>
• 방문 :전국 14개 지방병무청 병역진로설계지원센터(군지원센터)<br>
<br>
02. 병역설계(지방병무청 병역진로설계지원센터, 군지원센터)<br>
&nbsp;병무청 전문상담관과 병무상담/설계<br>
• 취업맞춤특기병 선발자격 등 안내/맞춤상담<br>
• 지원신체검사(병역판정검사를 받은 사람은 생략)<br>
&nbsp;<br>
03. 적성ㆍ진로상담(고용센터)<br>
&nbsp;고용부 전문상담원과 적성 및 진로상담<br>
• 개인별 적성에 맞는 기술훈련 등 안내<br>
• 국민취업지원제도 참여대상 여부 확인<br>
&nbsp;<br>
04. 기술훈련(고용센터)<br>
&nbsp;국가기간ㆍ전략산업 중심의 기술훈련(사무ㆍ서비스분야 제외)<br>
• 훈련비 지원&nbsp;<br>
• 훈련을 마친 사람은 취업 관리<br>
&nbsp;<br>
05. 입영/연기(지방병무청 군지원센터, 병역진로설계지원센터)<br>
&nbsp;가급적 원하는 시기ㆍ분야로 입영(모집계획 범위 내)<br>
&nbsp;취업한 사람은 24세까지 입영 연기<br>
&nbsp;<br>
06. 군복무<br>
&nbsp;기술병으로 복무<br>
• 기술숙련, 자기개발<br>
• 자격취득, 학습기회 제공 등<br>
&nbsp;<br>
07. 취업 등 사회진출</p>

<div data-hjsonver="1.0" data-jsonlen="15130">※기술훈련을 마치고 지원한 사람은 상담 및 기술훈련이 생략되므로 '취업' 또는 '입영'할 수 있습니다.</div>

<p>- 기술훈련과정 : 국가기간·전략산업 직종훈련, 중소기업 친화직종훈련, 국가인적자원개발컨소시엄 채용예정자 훈련, 폴리텍 기능사양성과정 훈련,내일배움카드제 훈련 중 일부, 일학습병행제, 내일이룸학교 등 국가기관 또는 지방자치단체에서 주관하는 직업훈련 과정</p>
</div>

<div class="layout_h3">
<h3>지원 - 선발 - 입영절차</h3>



<table class="table_row">
	<caption>지원-선발-입영절차에 관한내용표이며 지원서접수, 병역설계, 적성.진로상담, 기술훈련, 입영연기/해소, 유의사항내용을 제공</caption>
	<tbody>
		<tr>
			<th scope="row">01. 지원서 접수</th>
			<td>
			<p><strong>지원서는 연중 접수 가능하며, 인터넷(병무청 홈페이지 - 병무민원포털 - 군지원) 또는 지방병무청 군지원센터(병역진로설계지원센터)를 방문하여 접수하면 됩니다.</strong></p>
			<ul class="list">
				<li>현역병 입영일자가 결정된 사람은 입영일 30일 전까지 지원가능하며, 별도로 입영일자연기신청서를 병적지 지방병무청에 제출하여야 합니다.</li>
				<li>지원 시 선택한 입영시기·부대·특기 등은 기술훈련분야 및 입영하는 해 입영계획에 따라 변경될 수 있음을 유의하시기 바랍니다.</li>
				<li>지원서 접수취소는 기술훈련이 시작되기 전까지 가능합니다.
				<ul>
					<li>접속경로 : 병무청 홈페이지 →&nbsp;병무민원포털 → 군지원→ 지원서 작성·수정·취소</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">02. 병역설계</th>
			<td>
			<p><strong>지원서를 접수하고 난 뒤 지방병무청 전문상담관(응시지역 지방병무청 군지원센터, 병역진로설계지원센터)과 대면하여 상담을 받아야 합니다.</strong></p>
			<p><strong>기한 내 상담이 불가한 경우는 취업맞춤특기병&nbsp;지원이 직권으로 취소됩니다.</strong></p>
			<ul class="list">
				<li>병역판정검사를 받지 아니한 사람은 현역병지원 신체검사를 받아야 합니다.</li>
				<li>대면상담을 마친 뒤 7일 이내 '취업맞춤특기병 지원확인서'를 교부받습니다.</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">03. 적성·진로 상담</th>
			<td><strong>응시지구 지방병무청장이 발행한 '취업맞춤특기병 지원확인서'를 지참하고 고용센터를 방문하여 고용노동부&nbsp;국민취업지원제도 등 기술훈련 참여가능 여부 및 본인의 적성·진로, 훈련분야 등을 상담 받습니다.</strong></td>
		</tr>
		<tr>
			<th scope="row">04. 기술훈련</th>
			<td>
			<ul class="list">
				<li><strong>기술훈련이 시작된 사람은 훈련기관장으로부터 '훈련참여(수료)확인서'를 발급받아 응시지역 지방병무청에 제출하여야 합니다.</strong>
				<ul>
					<li>기술훈련 시작은 지원서 접수일로부터 6월 이내이어야 합니다.</li>
				</ul>
				</li>
				<li><strong>기술훈련은 국가기간·전략산업 직종훈련을 중심으로 실시되며 훈련기간은 1년 이내입니다.</strong>
				<ul>
					<li>취업맞춤특기병 선발자는 훈련과정 등에 성실히 참여하여야 하며, 기술훈련을 성실히 참여하지 않거나 중도에 탈락되는 경우는 직권으로 선발취소됩니다.</li>
				</ul>
				</li>
				<li><strong>기술훈련을 마친 사람은 해당분야로 취업하거나 입영할 수 있습니다.</strong>
				<ul>
					<li>훈련수료 후 6월 이내 취업한 사람은 24세까지 입영연기할 수 있습니다.</li>
					<li>미취업자는 정해진 일자에 입영하여야 합니다.</li>
					<li>훈련수료 후&nbsp;빠른 입영을 원하는 사람은 '조기입영신청서'를 제출합니다.(가급적 훈련수료일로 부터 6월 내 입영 가능, 모집계획 범위 내)</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">05. 입영연기/해소</th>
			<td>
			<ul class="list">
				<li><strong>기술훈련을 마치고 취업한 사람은 24세까지 현역병 입영을 연기할 수 있습니다.</strong>
				<ul>
					<li>'재직증명서'를 첨부하여 '입영기일 연기신청서'를 제출하도록 합니다.</li>
				</ul>
				</li>
				<li><strong>입영연기자 중 입영을 희망하는 사람은 '입영기일 연기해소신청서'를 제출하면 됩니다.</strong>
				<ul>
					<li>입영연기가 해소되면 해소일로부터 3월 이내의 일자로 입영일자가 결정됩니다.</li>
					<li>접속경로 : 병무청 홈페이지 →&nbsp;병무민원포털 → 군지원→ 선발취소 및 입영연기 등&nbsp;- 취업맞춤특기병 입영연기(해소)신청</li>
				</ul>
				</li>
			</ul>
			</td>
		</tr>
		<tr>
			<th scope="row">유의사항</th>
			<td>취업맞춤특기병 지원 시는 고졸 이하(대학 중퇴 포함) 학력이었으나 입영일자가 결정되기 전까지 대학에 진학(수학)하는 경우는 취업맞춤특기병 선발이 직권으로 취소되니 유의하시기 바랍니다.<br>
			* 전문대 등 일부대학 진학ㆍ수학 제외</td>
		</tr>
	</tbody>
</table>
</div>
	                            <!-- 컨탠츠 페이지 끝 -->
	                        </div>"""
