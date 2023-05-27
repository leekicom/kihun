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