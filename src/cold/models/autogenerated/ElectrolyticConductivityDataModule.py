
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataSetModule import DataSet







class ElectrolyticConductivityData(DataSet):
    """
    Class representing the `ElectrolyticConductivityData` entity, which inherits from:
    - DataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_571c1ae9_c4bf_48ab_babf_536153d22a0b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrolyticConductivityData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrolyticConductivityData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_571c1ae9_c4bf_48ab_babf_536153d22a0b',
    
    class_name='ElectrolyticConductivityData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_571c1ae9_c4bf_48ab_babf_536153d22a0b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrolyticConductivityData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    