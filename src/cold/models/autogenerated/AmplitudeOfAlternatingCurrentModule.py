
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class AmplitudeOfAlternatingCurrent(ElectricCurrent, ElectrochemicalControlQuantity):
    """
    Class representing the `AmplitudeOfAlternatingCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10eb778d_da60_4832_a355_4ee74baea650'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmplitudeOfAlternatingCurrent'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmplitudeOfAlternatingCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10eb778d_da60_4832_a355_4ee74baea650',
    
    class_name='AmplitudeOfAlternatingCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_10eb778d_da60_4832_a355_4ee74baea650',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmplitudeOfAlternatingCurrent',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    