#!"c:\xampp\perl\bin\perl.exe"

print "Content-type: text/html\n\n";

use DBI;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use JSON;
use XML::Simple;
use Data::Dumper;

$dbh = DBI->connect("DBI:mysql:database=project;host=localhost",
                       "root", "",
                       {'RaiseError' => 1});

my $cgi = CGI->new;
my $data = decode_json($cgi->param("r"));
#my $data = $cgi->param("r");
print Dumper($data);
#print Dumper($data);
my $xml = XMLout($data,RootName => undef);
my $id = $data->{Character}[0]->{design}[0];
print $id;

#$json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

#$text = decode_json($json);
#print  Dumper($text);

$sth = $dbh->prepare("Select * from franklin where ID = '$id'");
$rows = $sth->execute();
if ($rows >= 1)
{
	print "Oops! Design No Already Present! Provide a different design no";	
}
else
{
	$sth = $dbh->prepare("INSERT into franklin values('$id', '$xml')");
	$sth->execute(); 
	print "XML Data inserted successfully!";
}