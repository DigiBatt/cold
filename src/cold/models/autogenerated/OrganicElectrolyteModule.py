
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonAqueousElectrolyteModule import NonAqueousElectrolyte



from .ElectrolyteSolutionModule import ElectrolyteSolution







class OrganicElectrolyte(NonAqueousElectrolyte, ElectrolyteSolution):
    """
    Class representing the `OrganicElectrolyte` entity, which inherits from:
    - NonAqueousElectrolyte, ElectrolyteSolution

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_564d31be_91cb_4a8f_8369_2a55f1180499'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OrganicElectrolyte'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OrganicElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_564d31be_91cb_4a8f_8369_2a55f1180499',
    
    class_name='OrganicElectrolyte',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_564d31be_91cb_4a8f_8369_2a55f1180499',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OrganicElectrolyte',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    