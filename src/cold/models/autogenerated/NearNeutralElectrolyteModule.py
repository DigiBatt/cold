
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AqueousElectrolyteModule import AqueousElectrolyte







class NearNeutralElectrolyte(AqueousElectrolyte):
    """
    Class representing the `NearNeutralElectrolyte` entity, which inherits from:
    - AqueousElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc205ac2_314e_415c_a2b6_b12e8359d54c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NearNeutralElectrolyte'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NearNeutralElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc205ac2_314e_415c_a2b6_b12e8359d54c',
    
    class_name='NearNeutralElectrolyte',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc205ac2_314e_415c_a2b6_b12e8359d54c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NearNeutralElectrolyte',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    