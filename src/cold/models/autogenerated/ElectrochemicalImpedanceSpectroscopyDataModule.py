
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataSetModule import DataSet







class ElectrochemicalImpedanceSpectroscopyData(DataSet):
    """
    Class representing the `ElectrochemicalImpedanceSpectroscopyData` entity, which inherits from:
    - DataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c052cab7_46eb_4a87_b7a4_05be2572db22'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalImpedanceSpectroscopyData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalImpedanceSpectroscopyData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c052cab7_46eb_4a87_b7a4_05be2572db22',
    
    class_name='ElectrochemicalImpedanceSpectroscopyData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c052cab7_46eb_4a87_b7a4_05be2572db22',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalImpedanceSpectroscopyData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    