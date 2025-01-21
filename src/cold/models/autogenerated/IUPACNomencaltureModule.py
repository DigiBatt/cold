
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalNomenclatureModule import ChemicalNomenclature







class IUPACNomencalture(ChemicalNomenclature):
    """
    Class representing the `IUPACNomencalture` entity, which inherits from:
    - ChemicalNomenclature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_91a0635a_a89a_46de_8928_04a777d145c7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IUPACNomencalture'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IUPACNomencalture(
    
    class_iri='https://w3id.org/emmo#EMMO_91a0635a_a89a_46de_8928_04a777d145c7',
    
    class_name='IUPACNomencalture',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_91a0635a_a89a_46de_8928_04a777d145c7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IUPACNomencalture',
        alias="class_name"
    )
    

    
    

    

    