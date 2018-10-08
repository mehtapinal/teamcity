# coding: utf-8

from teamcity.custom.model import TeamCityObject


# from teamcity.models.agent_requirements import AgentRequirements  # noqa: F401,E501
# from teamcity.models.agents import Agents  # noqa: F401,E501
# from teamcity.models.artifact_dependencies import ArtifactDependencies  # noqa: F401,E501
# from teamcity.models.build_type import BuildType  # noqa: F401,E501
# from teamcity.models.builds import Builds  # noqa: F401,E501
# from teamcity.models.features import Features  # noqa: F401,E501
# from teamcity.models.investigations import Investigations  # noqa: F401,E501
# from teamcity.models.links import Links  # noqa: F401,E501
# from teamcity.models.project import Project  # noqa: F401,E501
# from teamcity.models.properties import Properties  # noqa: F401,E501
# from teamcity.models.snapshot_dependencies import SnapshotDependencies  # noqa: F401,E501
# from teamcity.models.steps import Steps  # noqa: F401,E501
# from teamcity.models.triggers import Triggers  # noqa: F401,E501
# from teamcity.models.vcs_root_entries import VcsRootEntries  # noqa: F401,E501


class BuildType(TeamCityObject):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'agent_requirements': 'AgentRequirements',
        'artifact_dependencies': 'ArtifactDependencies',
        'builds': 'Builds',
        'compatible_agents': 'Agents',
        'description': 'str',
        'features': 'Features',
        'href': 'str',
        'id': 'str',
        'internal_id': 'str',
        'investigations': 'Investigations',
        'links': 'Links',
        'locator': 'str',
        'name': 'str',
        'parameters': 'Properties',
        'paused': 'bool',
        'project': 'Project',
        'project_id': 'str',
        'project_internal_id': 'str',
        'project_name': 'str',
        'settings': 'Properties',
        'snapshot_dependencies': 'SnapshotDependencies',
        'steps': 'Steps',
        'template': 'BuildType',
        'template_flag': 'bool',
        'triggers': 'Triggers',
        'uuid': 'str',
        'vcs_root_entries': 'VcsRootEntries',
        'web_url': 'str'
    }

    attribute_map = {
        'agent_requirements': 'agent-requirements',
        'artifact_dependencies': 'artifact-dependencies',
        'builds': 'builds',
        'compatible_agents': 'compatibleAgents',
        'description': 'description',
        'features': 'features',
        'href': 'href',
        'id': 'id',
        'internal_id': 'internalId',
        'investigations': 'investigations',
        'links': 'links',
        'locator': 'locator',
        'name': 'name',
        'parameters': 'parameters',
        'paused': 'paused',
        'project': 'project',
        'project_id': 'projectId',
        'project_internal_id': 'projectInternalId',
        'project_name': 'projectName',
        'settings': 'settings',
        'snapshot_dependencies': 'snapshot-dependencies',
        'steps': 'steps',
        'template': 'template',
        'template_flag': 'templateFlag',
        'triggers': 'triggers',
        'uuid': 'uuid',
        'vcs_root_entries': 'vcs-root-entries',
        'web_url': 'webUrl'
    }

    def __init__(self, agent_requirements=None, artifact_dependencies=None, builds=None, compatible_agents=None, description=None, features=None, href=None, id=None, internal_id=None, investigations=None, links=None, locator=None, name=None, parameters=None, paused=False, project=None, project_id=None, project_internal_id=None, project_name=None, settings=None, snapshot_dependencies=None, steps=None, template=None, template_flag=False, triggers=None, uuid=None, vcs_root_entries=None, web_url=None):  # noqa: E501
        """BuildType - a model defined in Swagger"""  # noqa: E501
        super(BuildType, self).__init__()

        self._agent_requirements = None
        self._artifact_dependencies = None
        self._builds = None
        self._compatible_agents = None
        self._description = None
        self._features = None
        self._href = None
        self._id = None
        self._internal_id = None
        self._investigations = None
        self._links = None
        self._locator = None
        self._name = None
        self._parameters = None
        self._paused = None
        self._project = None
        self._project_id = None
        self._project_internal_id = None
        self._project_name = None
        self._settings = None
        self._snapshot_dependencies = None
        self._steps = None
        self._template = None
        self._template_flag = None
        self._triggers = None
        self._uuid = None
        self._vcs_root_entries = None
        self._web_url = None
        self.discriminator = None

        if agent_requirements is not None:
            self.agent_requirements = agent_requirements
        if artifact_dependencies is not None:
            self.artifact_dependencies = artifact_dependencies
        if builds is not None:
            self.builds = builds
        if compatible_agents is not None:
            self.compatible_agents = compatible_agents
        if description is not None:
            self.description = description
        if features is not None:
            self.features = features
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if internal_id is not None:
            self.internal_id = internal_id
        if investigations is not None:
            self.investigations = investigations
        if links is not None:
            self.links = links
        if locator is not None:
            self.locator = locator
        if name is not None:
            self.name = name
        if parameters is not None:
            self.parameters = parameters
        if paused is not None:
            self.paused = paused
        if project is not None:
            self.project = project
        if project_id is not None:
            self.project_id = project_id
        if project_internal_id is not None:
            self.project_internal_id = project_internal_id
        if project_name is not None:
            self.project_name = project_name
        if settings is not None:
            self.settings = settings
        if snapshot_dependencies is not None:
            self.snapshot_dependencies = snapshot_dependencies
        if steps is not None:
            self.steps = steps
        if template is not None:
            self.template = template
        if template_flag is not None:
            self.template_flag = template_flag
        if triggers is not None:
            self.triggers = triggers
        if uuid is not None:
            self.uuid = uuid
        if vcs_root_entries is not None:
            self.vcs_root_entries = vcs_root_entries
        if web_url is not None:
            self.web_url = web_url

    @property
    def agent_requirements(self):
        """Gets the agent_requirements of this BuildType.  # noqa: E501


        :return: The agent_requirements of this BuildType.  # noqa: E501
        :rtype: AgentRequirements
        """
        return self._agent_requirements

    @agent_requirements.setter
    def agent_requirements(self, agent_requirements):
        """Sets the agent_requirements of this BuildType.


        :param agent_requirements: The agent_requirements of this BuildType.  # noqa: E501
        :type: AgentRequirements
        """

        self._agent_requirements = agent_requirements

    @property
    def artifact_dependencies(self):
        """Gets the artifact_dependencies of this BuildType.  # noqa: E501


        :return: The artifact_dependencies of this BuildType.  # noqa: E501
        :rtype: ArtifactDependencies
        """
        return self._artifact_dependencies

    @artifact_dependencies.setter
    def artifact_dependencies(self, artifact_dependencies):
        """Sets the artifact_dependencies of this BuildType.


        :param artifact_dependencies: The artifact_dependencies of this BuildType.  # noqa: E501
        :type: ArtifactDependencies
        """

        self._artifact_dependencies = artifact_dependencies

    @property
    def builds(self):
        """Gets the builds of this BuildType.  # noqa: E501


        :return: The builds of this BuildType.  # noqa: E501
        :rtype: Builds
        """
        return self._builds

    @builds.setter
    def builds(self, builds):
        """Sets the builds of this BuildType.


        :param builds: The builds of this BuildType.  # noqa: E501
        :type: Builds
        """

        self._builds = builds

    @property
    def compatible_agents(self):
        """Gets the compatible_agents of this BuildType.  # noqa: E501


        :return: The compatible_agents of this BuildType.  # noqa: E501
        :rtype: Agents
        """
        return self._compatible_agents

    @compatible_agents.setter
    def compatible_agents(self, compatible_agents):
        """Sets the compatible_agents of this BuildType.


        :param compatible_agents: The compatible_agents of this BuildType.  # noqa: E501
        :type: Agents
        """

        self._compatible_agents = compatible_agents

    @property
    def description(self):
        """Gets the description of this BuildType.  # noqa: E501


        :return: The description of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BuildType.


        :param description: The description of this BuildType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def features(self):
        """Gets the features of this BuildType.  # noqa: E501


        :return: The features of this BuildType.  # noqa: E501
        :rtype: Features
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BuildType.


        :param features: The features of this BuildType.  # noqa: E501
        :type: Features
        """

        self._features = features

    @property
    def href(self):
        """Gets the href of this BuildType.  # noqa: E501


        :return: The href of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BuildType.


        :param href: The href of this BuildType.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this BuildType.  # noqa: E501


        :return: The id of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BuildType.


        :param id: The id of this BuildType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_id(self):
        """Gets the internal_id of this BuildType.  # noqa: E501


        :return: The internal_id of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this BuildType.


        :param internal_id: The internal_id of this BuildType.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def investigations(self):
        """Gets the investigations of this BuildType.  # noqa: E501


        :return: The investigations of this BuildType.  # noqa: E501
        :rtype: Investigations
        """
        return self._investigations

    @investigations.setter
    def investigations(self, investigations):
        """Sets the investigations of this BuildType.


        :param investigations: The investigations of this BuildType.  # noqa: E501
        :type: Investigations
        """

        self._investigations = investigations

    @property
    def links(self):
        """Gets the links of this BuildType.  # noqa: E501


        :return: The links of this BuildType.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BuildType.


        :param links: The links of this BuildType.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def locator(self):
        """Gets the locator of this BuildType.  # noqa: E501


        :return: The locator of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this BuildType.


        :param locator: The locator of this BuildType.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def name(self):
        """Gets the name of this BuildType.  # noqa: E501


        :return: The name of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildType.


        :param name: The name of this BuildType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this BuildType.  # noqa: E501


        :return: The parameters of this BuildType.  # noqa: E501
        :rtype: Properties
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BuildType.


        :param parameters: The parameters of this BuildType.  # noqa: E501
        :type: Properties
        """

        self._parameters = parameters

    @property
    def paused(self):
        """Gets the paused of this BuildType.  # noqa: E501


        :return: The paused of this BuildType.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this BuildType.


        :param paused: The paused of this BuildType.  # noqa: E501
        :type: bool
        """

        self._paused = paused

    @property
    def project(self):
        """Gets the project of this BuildType.  # noqa: E501


        :return: The project of this BuildType.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this BuildType.


        :param project: The project of this BuildType.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def project_id(self):
        """Gets the project_id of this BuildType.  # noqa: E501


        :return: The project_id of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BuildType.


        :param project_id: The project_id of this BuildType.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_internal_id(self):
        """Gets the project_internal_id of this BuildType.  # noqa: E501


        :return: The project_internal_id of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._project_internal_id

    @project_internal_id.setter
    def project_internal_id(self, project_internal_id):
        """Sets the project_internal_id of this BuildType.


        :param project_internal_id: The project_internal_id of this BuildType.  # noqa: E501
        :type: str
        """

        self._project_internal_id = project_internal_id

    @property
    def project_name(self):
        """Gets the project_name of this BuildType.  # noqa: E501


        :return: The project_name of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this BuildType.


        :param project_name: The project_name of this BuildType.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def settings(self):
        """Gets the settings of this BuildType.  # noqa: E501


        :return: The settings of this BuildType.  # noqa: E501
        :rtype: Properties
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this BuildType.


        :param settings: The settings of this BuildType.  # noqa: E501
        :type: Properties
        """

        self._settings = settings

    @property
    def snapshot_dependencies(self):
        """Gets the snapshot_dependencies of this BuildType.  # noqa: E501


        :return: The snapshot_dependencies of this BuildType.  # noqa: E501
        :rtype: SnapshotDependencies
        """
        return self._snapshot_dependencies

    @snapshot_dependencies.setter
    def snapshot_dependencies(self, snapshot_dependencies):
        """Sets the snapshot_dependencies of this BuildType.


        :param snapshot_dependencies: The snapshot_dependencies of this BuildType.  # noqa: E501
        :type: SnapshotDependencies
        """

        self._snapshot_dependencies = snapshot_dependencies

    @property
    def steps(self):
        """Gets the steps of this BuildType.  # noqa: E501


        :return: The steps of this BuildType.  # noqa: E501
        :rtype: Steps
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this BuildType.


        :param steps: The steps of this BuildType.  # noqa: E501
        :type: Steps
        """

        self._steps = steps

    @property
    def template(self):
        """Gets the template of this BuildType.  # noqa: E501


        :return: The template of this BuildType.  # noqa: E501
        :rtype: BuildType
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this BuildType.


        :param template: The template of this BuildType.  # noqa: E501
        :type: BuildType
        """

        self._template = template

    @property
    def template_flag(self):
        """Gets the template_flag of this BuildType.  # noqa: E501


        :return: The template_flag of this BuildType.  # noqa: E501
        :rtype: bool
        """
        return self._template_flag

    @template_flag.setter
    def template_flag(self, template_flag):
        """Sets the template_flag of this BuildType.


        :param template_flag: The template_flag of this BuildType.  # noqa: E501
        :type: bool
        """

        self._template_flag = template_flag

    @property
    def triggers(self):
        """Gets the triggers of this BuildType.  # noqa: E501


        :return: The triggers of this BuildType.  # noqa: E501
        :rtype: Triggers
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this BuildType.


        :param triggers: The triggers of this BuildType.  # noqa: E501
        :type: Triggers
        """

        self._triggers = triggers

    @property
    def uuid(self):
        """Gets the uuid of this BuildType.  # noqa: E501


        :return: The uuid of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this BuildType.


        :param uuid: The uuid of this BuildType.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def vcs_root_entries(self):
        """Gets the vcs_root_entries of this BuildType.  # noqa: E501


        :return: The vcs_root_entries of this BuildType.  # noqa: E501
        :rtype: VcsRootEntries
        """
        return self._vcs_root_entries

    @vcs_root_entries.setter
    def vcs_root_entries(self, vcs_root_entries):
        """Sets the vcs_root_entries of this BuildType.


        :param vcs_root_entries: The vcs_root_entries of this BuildType.  # noqa: E501
        :type: VcsRootEntries
        """

        self._vcs_root_entries = vcs_root_entries

    @property
    def web_url(self):
        """Gets the web_url of this BuildType.  # noqa: E501


        :return: The web_url of this BuildType.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this BuildType.


        :param web_url: The web_url of this BuildType.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

