
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VariableModule import Variable







class NumericalVariable(Variable):
    """
    Class representing the `NumericalVariable` entity, which inherits from:
    - Variable

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9e029526_79a2_47a8_a151_dd0545db471b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumericalVariable'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumericalVariable(
    
    class_iri='https://w3id.org/emmo#EMMO_9e029526_79a2_47a8_a151_dd0545db471b',
    
    class_name='NumericalVariable',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9e029526_79a2_47a8_a151_dd0545db471b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumericalVariable',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    