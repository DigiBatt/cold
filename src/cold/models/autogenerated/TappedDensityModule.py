
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DensityModule import Density







class TappedDensity(Density):
    """
    Class representing the `TappedDensity` entity, which inherits from:
    - Density

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5ce6a328_713c_4383_ad63_26c902c30e34'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TappedDensity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TappedDensity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5ce6a328_713c_4383_ad63_26c902c30e34',
    
    class_name='TappedDensity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5ce6a328_713c_4383_ad63_26c902c30e34',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TappedDensity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    