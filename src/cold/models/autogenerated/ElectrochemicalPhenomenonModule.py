
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalPhenomenonModule import PhysicalPhenomenon







class ElectrochemicalPhenomenon(PhysicalPhenomenon):
    """
    Class representing the `ElectrochemicalPhenomenon` entity, which inherits from:
    - PhysicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_19abaccd_43be_4048_965c_e4fb63c5951b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalPhenomenon'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalPhenomenon(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_19abaccd_43be_4048_965c_e4fb63c5951b',
    
    class_name='ElectrochemicalPhenomenon',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_19abaccd_43be_4048_965c_e4fb63c5951b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalPhenomenon',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    