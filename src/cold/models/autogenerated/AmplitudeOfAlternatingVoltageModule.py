
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialModule import ElectricPotential



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class AmplitudeOfAlternatingVoltage(ElectricPotential, ElectrochemicalControlQuantity):
    """
    Class representing the `AmplitudeOfAlternatingVoltage` entity, which inherits from:
    - ElectricPotential, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f591a444_89d6_4093_836d_7d53895edce4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmplitudeOfAlternatingVoltage'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmplitudeOfAlternatingVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f591a444_89d6_4093_836d_7d53895edce4',
    
    class_name='AmplitudeOfAlternatingVoltage',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f591a444_89d6_4093_836d_7d53895edce4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmplitudeOfAlternatingVoltage',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    