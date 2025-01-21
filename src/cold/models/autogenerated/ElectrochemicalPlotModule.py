
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RepresentationModule import Representation







class ElectrochemicalPlot(Representation):
    """
    Class representing the `ElectrochemicalPlot` entity, which inherits from:
    - Representation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ddade648_2033_47b6_bc36_b562a9af591e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalPlot'`
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
    obj = ElectrochemicalPlot(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ddade648_2033_47b6_bc36_b562a9af591e',
    
    class_name='ElectrochemicalPlot',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ddade648_2033_47b6_bc36_b562a9af591e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalPlot',
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
    

    
    

    

    